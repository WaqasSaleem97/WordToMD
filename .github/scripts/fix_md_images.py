#!/usr/bin/env python3
"""
.github/scripts/fix_md_images.py

Post-process a Markdown file to ensure images are on their own paragraph
and moved after any paragraph text they were accidentally inlined into.

Behavior:
- For each paragraph-block (blocks separated by one or more blank lines):
  - If the block contains both text and one or more images (HTML <img ...> or Markdown ![alt](src)),
    remove the image tokens from the block, keep the text as the paragraph, then append each image
    as its own paragraph immediately after the paragraph text (preserving their original order).
  - If the block contains only images, leave it as-is (one image per paragraph).
  - If the block contains no images, keep it unchanged.

Usage:
  # Show transformed output
  python3 .github/scripts/fix_md_images.py converted/file.md

  # Overwrite file in-place
  python3 .github/scripts/fix_md_images.py converted/file.md --inplace
"""
from pathlib import Path
import re
import sys

# Combined pattern that matches HTML <img ...> (non-greedy) OR Markdown images ![alt](url)
IMG_COMBINED_RE = re.compile(r'(<img\b[\s\S]*?>|!\[[^\]]*\]\([^\)]+\))', re.I)

# Splits blocks by one or more blank lines (keeps internal newlines in a block)
BLOCK_SPLIT_RE = re.compile(r'\n\s*\n', re.M)

def process_text(text: str) -> str:
    blocks = BLOCK_SPLIT_RE.split(text)
    out_blocks = []

    for block in blocks:
        if not block.strip():
            # preserve empty blocks as empty (they will be collapsed later)
            out_blocks.append('')
            continue

        # find images and their positions (ordered)
        matches = list(IMG_COMBINED_RE.finditer(block))
        if not matches:
            out_blocks.append(block)
            continue

        # Extract images in order
        images = [m.group(0).strip() for m in matches]

        # Remove matched image substrings from the block by replacing them with a single space
        # Doing replacements from end->start to preserve indices
        new_block = block
        for m in reversed(matches):
            start, end = m.start(), m.end()
            # replace slice with a single space to avoid accidental word concatenation
            new_block = new_block[:start] + ' ' + new_block[end:]

        # Normalize whitespace
        new_block = new_block.strip()
        # If new_block still has textual content, keep it as the paragraph first
        if new_block:
            out_blocks.append(new_block)
            # append each image as a separate paragraph block
            for img in images:
                out_blocks.append(img)
        else:
            # block had only images (or images + whitespace). Keep each image as its own paragraph
            for img in images:
                out_blocks.append(img)

    # Rejoin blocks with exactly two newlines between blocks, then collapse 3+ newlines to 2
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
