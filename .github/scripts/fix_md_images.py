#!/usr/bin/env python3
"""
.github/scripts/fix_md_images.py

Move leading <img...> (HTML) or leading markdown images that are
at the start of a paragraph block to a separate block immediately
after that paragraph.

This updated version also handles images that are immediately followed
(with no whitespace) by a triple-asterisk bold paragraph like:

<img .../>***Open VMware ...***

Usage:
  python3 .github/scripts/fix_md_images.py converted/yourfile.md --inplace
"""
import re
import sys
from pathlib import Path

# Matches an HTML <img ...> tag (single or multiple)
IMG_HTML_RE = re.compile(r'(?P<img><img\b[^>]*\/?>)', re.I | re.S)
# Matches leading HTML img(s) at start of block (possibly with attributes broken across lines)
LEADING_IMG_HTML_BLOCK = re.compile(r'^\s*(?P<img>(?:<img\b[^>]*\/?>\s*)+)(?P<rest>[\s\S]*)$', re.I)
# Matches leading Markdown images at start of block
LEADING_IMG_MD_BLOCK = re.compile(r'^\s*(?P<img>(?:!\[[^\]]*\]\([^\)]+\)\s*)+)(?P<rest>[\s\S]*)$', re.I)

# Specific pattern: img immediately followed by triple-asterisk bold (no space)
IMG_PLUS_TRIPLE_ASTERISK = re.compile(r'^\s*(?P<img><img\b[^>]*\/?>)\s*(?P<triple>\*{3}[\s\S]*?\*{3})(?P<rest>[\s\S]*)$', re.I)

def process_text(text: str) -> str:
    # Split into blocks separated by one or more blank lines (preserve internal newlines)
    blocks = re.split(r'\n\s*\n', text)
    out_blocks = []

    for block in blocks:
        # 0) Specific: image immediately followed by ***...*** (no space may be present)
        m_spec = IMG_PLUS_TRIPLE_ASTERISK.match(block)
        if m_spec:
            img = m_spec.group('img').strip()
            triple = m_spec.group('triple').strip()
            rest = m_spec.group('rest').lstrip()
            # Desired order: triple block, (rest if any), then image block on separate paragraph
            if rest:
                out_blocks.append(f"{triple}\n\n{rest}")
            else:
                out_blocks.append(triple)
            out_blocks.append(img)
            continue

        # 1) Leading HTML <img> tags in same block
        m = LEADING_IMG_HTML_BLOCK.match(block)
        if m:
            img = m.group('img').strip()
            rest = m.group('rest').lstrip()
            if rest:
                out_blocks.append(rest)
                out_blocks.append(img)
            else:
                out_blocks.append(img)
            continue

        # 2) Leading Markdown images in same block
        m2 = LEADING_IMG_MD_BLOCK.match(block)
        if m2:
            img = m2.group('img').strip()
            rest = m2.group('rest').lstrip()
            if rest:
                out_blocks.append(rest)
                out_blocks.append(img)
            else:
                out_blocks.append(img)
            continue

        # 3) If no leading image, keep block as-is
        out_blocks.append(block)

    # Rejoin with two newlines and collapse any 3+ newlines down to 2
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
