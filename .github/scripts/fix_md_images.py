#!/usr/bin/env python3
"""
.github/scripts/fix_md_images.py

Post-process a Markdown file so:
- multi-line HTML <img ...> tags are normalized to a single-line tag,
- paragraphs that contain both text and images are split so the text stays first
  and each image becomes its own paragraph immediately after,
- WHEN the paragraph is a blockquote (lines starting with '>'), the moved image
  paragraph(s) are kept inside the same blockquote (each line prefixed with '> ').

Usage:
  python3 .github/scripts/fix_md_images.py converted/file.md --inplace
"""
from pathlib import Path
import re
import sys

# Match HTML <img ...> (non-greedy, across newlines)
RE_IMG_TAG = re.compile(r'<img\b[\s\S]*?>', re.I)
# Match Markdown image syntax
RE_IMG_MD = re.compile(r'!\[[^\]]*\]\([^\)]+\)', re.I)
# Combined matcher for either HTML or markdown image tokens
RE_IMG_COMBINED = re.compile(r'(<img\b[\s\S]*?>|!\[[^\]]*\]\([^\)]+\))', re.I)

# Split blocks by one or more blank lines (preserve internal newlines)
BLOCK_SPLIT_RE = re.compile(r'\n\s*\n', re.M)

def normalize_img_tags(text: str) -> str:
    """Collapse any HTML <img ...> tag spanning multiple lines into a single-line tag."""
    def repl(m):
        tag = m.group(0)
        # Replace internal whitespace (including newlines) with single spaces
        norm = re.sub(r'\s+', ' ', tag)
        return norm.strip()
    return RE_IMG_TAG.sub(repl, text)

def split_into_blocks(text: str):
    """Return list of blocks (preserving original block strings)."""
    return BLOCK_SPLIT_RE.split(text)

def process_block_plain(block: str):
    """
    For a non-blockquote block: extract images (HTML or markdown) and separate them.
    Returns list of blocks where textual content appears first (if any) followed by each image
    as its own block.
    """
    if not block.strip():
        return ['']
    matches = list(RE_IMG_COMBINED.finditer(block))
    if not matches:
        return [block]

    # Extract images in order
    images = [m.group(0).strip() for m in matches]

    # Remove all image tokens from the block; replace each with a single space
    new_block = block
    for m in reversed(matches):
        s, e = m.start(), m.end()
        new_block = new_block[:s] + ' ' + new_block[e:]
    new_block = new_block.strip()

    out = []
    if new_block:
        out.append(new_block)
        out.extend(images)
    else:
        out.extend(images)
    return out

def process_block_blockquote(block: str):
    """
    Handle blockquote block: strip a single leading '> ' from each line to get inner text,
    process inner text with process_block_plain, then re-prefix each output block line with '> '.
    """
    lines = block.splitlines()
    # remove leading '>' and one optional following space from each line
    inner_lines = [re.sub(r'^\s*>\s?', '', ln) for ln in lines]
    inner_text = '\n'.join(inner_lines)
    # process inner text to separate paragraph and images
    inner_out_blocks = process_block_plain(inner_text)
    # prefix each resulting block with '> ' per line
    prefixed_blocks = []
    for b in inner_out_blocks:
        # prefix each line of the block with '> '
        prefixed = '\n'.join([f'> {ln}' if ln.strip() != '' else '>' for ln in b.splitlines()])
        # if the block is single-line and empty, keep '>' to maintain quote line
        prefixed_blocks.append(prefixed)
    return prefixed_blocks

def process_text(text: str) -> str:
    # First normalize multi-line <img> to single-line tags
    text = normalize_img_tags(text)

    blocks = split_into_blocks(text)
    out_blocks = []

    for block in blocks:
        if not block.strip():
            out_blocks.append('')
            continue

        # detect blockquote: if first non-empty line starts with '>'
        first_line = next((ln for ln in block.splitlines() if ln.strip() != ''), '')
        if first_line.startswith('>'):
            processed = process_block_blockquote(block)
            out_blocks.extend(processed)
        else:
            processed = process_block_plain(block)
            out_blocks.extend(processed)

    # Rejoin blocks with exactly two newlines and collapse any 3+ newlines to 2
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
