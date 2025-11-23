#!/usr/bin/env python3
"""
fix_md_images.py <file.md>

Move leading <img...> (HTML) or leading markdown images that are
at the start of a paragraph block to a separate block immediately
after that paragraph.

Usage:
  # print transformed markdown to stdout
  python3 .github/scripts/fix_md_images.py converted/CC-Lab4-Sarosh059.md

  # overwrite file in place
  python3 .github/scripts/fix_md_images.py converted/CC-Lab4-Sarosh059.md --inplace
"""
import re
import sys
from pathlib import Path

IMG_HTML_RE = re.compile(r'^\s*(?P<img>(?:<img\b[^>]*>)+)\s*(?P<rest>[\s\S]*)$', re.I)
IMG_MD_RE   = re.compile(r'^\s*(?P<img>(?:!\[[^\]]*\]\([^\)]+\)\s*)+)(?P<rest>[\s\S]*)$', re.I)

def process_text(text: str) -> str:
    # Split into blocks by blank lines (one or more). Preserve leading/trailing whitespace inside blocks.
    blocks = re.split(r'\n\s*\n', text)
    out_blocks = []

    for block in blocks:
        # Try HTML <img> leading
        m = IMG_HTML_RE.match(block)
        if m:
            img = m.group('img').rstrip()
            rest = m.group('rest').lstrip()
            if rest:  # leading image + text in same block -> move image AFTER the paragraph
                # append paragraph (rest) then image as its own block
                out_blocks.append(rest)
                out_blocks.append(img)
                continue
            else:
                # block is image-only, keep as-is
                out_blocks.append(img)
                continue

        # Try markdown image leading
        m2 = IMG_MD_RE.match(block)
        if m2:
            img = m2.group('img').rstrip()
            rest = m2.group('rest').lstrip()
            if rest:
                out_blocks.append(rest)
                out_blocks.append(img)
                continue
            else:
                out_blocks.append(img)
                continue

        # No leading image, keep block unchanged
        out_blocks.append(block)

    # Rejoin with two newlines between blocks, then normalize any 3+ newlines down to 2
    out = '\n\n'.join(out_blocks)
    out = re.sub(r'\n{3,}', '\n\n', out)
    return out

def main():
    if len(sys.argv) < 2:
        print("Usage: fix_md_images.py <file.md> [--inplace]", file=sys.stderr)
        sys.exit(2)

    path = Path(sys.argv[1])
    inplace = '--inplace' in sys.argv[2:]

    if not path.is_file():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding='utf-8')
    newtext = process_text(text)

    if inplace:
        path.write_text(newtext, encoding='utf-8')
        print(f"Processed and overwrote: {path}")
    else:
        sys.stdout.write(newtext)

if __name__ == '__main__':
    main()
