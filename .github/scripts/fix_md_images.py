#!/usr/bin/env python3
"""
.github/scripts/fix_md_images.py

Robust post-processor for Markdown produced by pandoc.

Fixes two problems:
1) HTML <img ...> tags that are split across lines (attributes on next lines)
   get normalized to a single-line tag so they don't leave attribute fragments
   in the paragraph when we extract images.
2) Paragraphs that contain both text and images (HTML <img...> or Markdown ![](...))
   are split so the paragraph text stays first and each image becomes its own
   paragraph immediately after (preserving original order).

Usage:
  # Show transformed output
  python3 .github/scripts/fix_md_images.py converted/file.md

  # Overwrite file in-place
  python3 .github/scripts/fix_md_images.py converted/file.md --inplace
"""
from pathlib import Path
import re
import sys

# Matches an HTML <img ...> tag (non-greedy, across newlines)
RE_IMG_TAG = re.compile(r'<img\b[\s\S]*?>', re.I)
# Matches Markdown image syntax ![alt](url)
RE_IMG_MD = re.compile(r'!\[[^\]]*\]\([^\)]+\)', re.I)
# Combined matcher to find either HTML or markdown images in a block
RE_IMG_COMBINED = re.compile(r'(<img\b[\s\S]*?>|!\[[^\]]*\]\([^\)]+\))', re.I)

# Split blocks by one or more blank lines (preserve internal newlines)
BLOCK_SPLIT_RE = re.compile(r'\n\s*\n', re.M)

def normalize_img_tags(text: str) -> str:
    """
    Collapse any HTML <img ...> tag that spans multiple lines into a single line,
    normalizing whitespace inside the tag. This prevents attribute fragments
    from being left behind when removing/moving images.
    """
    def repl(m):
        tag = m.group(0)
        # Replace internal whitespace (including newlines) with single spaces
        norm = re.sub(r'\s+', ' ', tag)
        return norm.strip()
    return RE_IMG_TAG.sub(repl, text)

def process_text(text: str) -> str:
    # First, normalize any multi-line <img ...> tags so tags are self-contained single-line tokens.
    text = normalize_img_tags(text)

    blocks = BLOCK_SPLIT_RE.split(text)
    out_blocks = []

    for block in blocks:
        if not block.strip():
            # preserve empty blocks as empty string (will be collapsed later)
            out_blocks.append('')
            continue

        # Find images (HTML or Markdown) in this block in order
        matches = list(RE_IMG_COMBINED.finditer(block))
        if not matches:
            out_blocks.append(block)
            continue

        # Extract image tokens in order
        images = [m.group(0).strip() for m in matches]

        # Remove all image tokens from the block; replace each with a single space to avoid word joining
        new_block = block
        for m in reversed(matches):
            s, e = m.start(), m.end()
            new_block = new_block[:s] + ' ' + new_block[e:]

        # Normalize whitespace and trim
        new_block = new_block.strip()
        # If textual content remains, keep it as the paragraph first, then append images each as its own paragraph
        if new_block:
            out_blocks.append(new_block)
            for img in images:
                out_blocks.append(img)
        else:
            # Block had only images (or images + whitespace): make each image its own paragraph
            for img in images:
                out_blocks.append(img)

    # Rejoin blocks with exactly two newlines between them and collapse any 3+ newlines -> 2
    out = '\n\n'.join([b for b in out_blocks if b is not None])
    out = re.sub(r'\n{3,}', '\n\n', out)
    return out

def main():
    if len(sys.argv) < 2:
        print("Usage: fix_md_images.py <file.md> [--inplace]", file=sys.stderr)
        sys.exit(2)

    path = Path(sys.argv[1])
    inplace = '--inplace' in sys.argv[2:]

    if not path.exists() or not path.is_file():
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
