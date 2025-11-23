#!/usr/bin/env python3
"""
.github/scripts/fix_pandoc_ast.py

Reads pandoc JSON AST input file and writes a fixed JSON that moves image-only
blocks (Para/Plain containing only Image/RawInline <img> or RawBlock with <img>)
that appear immediately BEFORE a text paragraph, so the paragraph comes first
and the image block after it.

Usage:
  python3 .github/scripts/fix_pandoc_ast.py in.json out.json
"""
import json
import sys

def is_image_inline(inline):
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

def block_is_image_only(block):
    if not isinstance(block, list) or len(block) == 0:
        return False
    tag = block[0]
    if tag in ("Para", "Plain"):
        inlines = block[1] if len(block) > 1 else []
        if not isinstance(inlines, list):
            return False
        # consider image-only if every non-space inline is Image or RawInline <img>
        for inline in inlines:
            if isinstance(inline, list) and inline and inline[0] == "Space":
                continue
            if not is_image_inline(inline):
                return False
        return True
    if tag == "RawBlock":
        # RawBlock: ["RawBlock", format, string]
        if len(block) >= 3 and isinstance(block[2], str) and "<img" in block[2].lower():
            return True
    return False

def block_is_text_paragraph(block):
    if not isinstance(block, list) or len(block) == 0:
        return False
    tag = block[0]
    if tag not in ("Para", "Plain"):
        return False
    inlines = block[1] if len(block) > 1 else []
    if not isinstance(inlines, list) or len(inlines) == 0:
        return False
    for inline in inlines:
        # skip spaces
        if isinstance(inline, list) and inline and inline[0] == "Space":
            continue
        if isinstance(inline, list) and inline:
            if inline[0] in ("Str", "Strong", "Emph", "Code", "Link", "Span"):
                return True
            if inline[0] == "RawInline":
                return True
    return False

def process_blocks(blocks):
    # Repeatedly scan and swap image-only blocks that precede text paragraphs.
    while True:
        swapped = False
        i = 0
        while i < len(blocks) - 1:
            b = blocks[i]
            nb = blocks[i+1]
            if block_is_image_only(b) and block_is_text_paragraph(nb):
                # swap
                blocks[i], blocks[i+1] = nb, b
                swapped = True
                i = max(i - 1, 0)
            else:
                i += 1
        if not swapped:
            break
    return blocks

def main(inp_path, out_path):
    with open(inp_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "blocks" in data:
        data["blocks"] = process_blocks(data["blocks"])
    elif isinstance(data, list):
        # treat top-level as blocks
        data = process_blocks(data)
    else:
        print("Unexpected pandoc JSON layout: expected object with 'blocks' or a list.", file=sys.stderr)
        sys.exit(1)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: fix_pandoc_ast.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
