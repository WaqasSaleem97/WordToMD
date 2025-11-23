#!/usr/bin/env python3
"""
.github/scripts/fix_pandoc_ast.py

Fix pandoc JSON AST so images that appear before paragraph text become
placed after the paragraph.

This script:
- swaps image-only blocks that precede text paragraphs (existing behavior)
- ALSO: if a Para/Plain block begins with image-like inlines (Image or RawInline <img>)
  followed by textual content in the same Para, it removes those leading image inlines
  and inserts them as a new Para immediately after the original paragraph.

Usage:
  python3 .github/scripts/fix_pandoc_ast.py in.json out.json
"""
import json
import sys
from copy import deepcopy

def is_image_inline(inline):
    """Return True if inline is an Image or RawInline containing <img>."""
    if not isinstance(inline, list) or len(inline) == 0:
        return False
    tag = inline[0]
    if tag == "Image":
        return True
    if tag == "RawInline":
        # RawInline: ["RawInline", format, content]
        if len(inline) >= 3 and isinstance(inline[2], str) and "<img" in inline[2].lower():
            return True
    return False

def is_space_inline(inline):
    return isinstance(inline, list) and inline and inline[0] == "Space"

def block_is_image_only(block):
    """Return True for Para/Plain all images, or RawBlock with <img>."""
    if not isinstance(block, list) or len(block) == 0:
        return False
    tag = block[0]
    if tag in ("Para", "Plain"):
        inlines = block[1] if len(block) > 1 else []
        if not isinstance(inlines, list):
            return False
        for inline in inlines:
            if is_space_inline(inline):
                continue
            if not is_image_inline(inline):
                return False
        return True
    if tag == "RawBlock":
        if len(block) >= 3 and isinstance(block[2], str) and "<img" in block[2].lower():
            return True
    return False

def block_is_text_paragraph(block):
    """Return True if block is a paragraph-like block that begins with textual content."""
    if not isinstance(block, list) or len(block) == 0:
        return False
    tag = block[0]
    if tag not in ("Para", "Plain"):
        return False
    inlines = block[1] if len(block) > 1 else []
    if not isinstance(inlines, list) or len(inlines) == 0:
        return False
    for inline in inlines:
        if is_space_inline(inline):
            continue
        if isinstance(inline, list) and inline:
            if inline[0] in ("Str", "Strong", "Emph", "Code", "Link", "Span"):
                return True
            if inline[0] == "RawInline":
                # treat RawInline as text if it isn't an <img>
                if not (len(inline) >= 3 and isinstance(inline[2], str) and "<img" in inline[2].lower()):
                    return True
    return False

def process_blocks_swap_image_blocks(blocks):
    """Repeatedly swap image-only blocks that precede text paragraphs."""
    while True:
        swapped = False
        i = 0
        while i < len(blocks) - 1:
            b = blocks[i]
            nb = blocks[i+1]
            if block_is_image_only(b) and block_is_text_paragraph(nb):
                blocks[i], blocks[i+1] = nb, b
                swapped = True
                i = max(i - 1, 0)
            else:
                i += 1
        if not swapped:
            break
    return blocks

def move_leading_images_within_paras(blocks):
    """
    For each Para/Plain: if leading inlines (ignoring spaces) are image-like
    and the Para contains textual inline(s) later, remove those leading image
    inlines and insert a new Para with those images immediately after the current Para.
    """
    i = 0
    while i < len(blocks):
        block = blocks[i]
        if isinstance(block, list) and len(block) > 0 and block[0] in ("Para", "Plain"):
            inlines = block[1] if len(block) > 1 else []
            if isinstance(inlines, list) and len(inlines) > 0:
                # find index of first non-space inline
                idx = 0
                while idx < len(inlines) and is_space_inline(inlines[idx]):
                    idx += 1
                # collect leading image-like inlines starting at first non-space
                lead_start = idx
                lead_end = lead_start
                while lead_end < len(inlines) and is_image_inline(inlines[lead_end]):
                    lead_end += 1
                # if we have at least one leading image and there remains textual content after
                if lead_end > lead_start and lead_end < len(inlines):
                    # build leading list without surrounding spaces
                    leading = []
                    # if there were spaces between images, keep no extra spaces
                    for k in range(lead_start, lead_end):
                        leading.append(inlines[k])
                    # remove leading slice (and any immediately following spaces)
                    remaining = []
                    # keep all inlines after lead_end
                    remaining = inlines[lead_end:]
                    # Update current block to remaining inlines (but preserve initial spaces if any)
                    # If there were spaces before lead_start, keep them
                    prefix_spaces = [x for x in inlines[:lead_start] if is_space_inline(x)]
                    blocks[i][1] = prefix_spaces + remaining
                    # create new Para block for the images (put images in same inline structure)
                    new_para = ["Para", leading]
                    blocks.insert(i+1, new_para)
                    # move index past the newly inserted para
                    i += 1
        i += 1
    return blocks

def process_blocks(blocks):
    # First swap separate image-only blocks
    blocks = process_blocks_swap_image_blocks(blocks)
    # Then handle leading image inlines inside paragraphs
    blocks = move_leading_images_within_paras(blocks)
    # After moving, do another pass of swapping to catch newly adjacent image-blocks
    blocks = process_blocks_swap_image_blocks(blocks)
    return blocks

def main(inp_path, out_path):
    with open(inp_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "blocks" in data:
        data["blocks"] = process_blocks(data["blocks"])
    elif isinstance(data, list):
        data = process_blocks(data)
    else:
        print("Unexpected pandoc JSON layout: expected object with 'blocks' or a list.", file=sys.stderr)
        sys.exit(1)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: fix_pandoc_ast.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
