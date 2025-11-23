#!/usr/bin/env python3
"""
fix_pandoc_ast.py <input.json> <output.json>

Reads pandoc JSON AST, moves image-only blocks (Para/Plain consisting only of Images or RawInline <img>)
or RawBlock html <img> blocks that appear immediately BEFORE a text paragraph, so that the paragraph comes
first and the image block comes after it.

This is a conservative heuristic designed to fix the common case you reported.
"""
import json
import sys

def is_image_inline(inline):
    # inline is a list like ["Image", alt, [attr, src, title]] or ["RawInline", fmt, str]
    if not isinstance(inline, list) or len(inline) == 0:
        return False
    tag = inline[0]
    if tag == "Image":
        return True
    if tag == "RawInline":
        # inline[2] or inline[1]? Pandoc JSON RawInline is ["RawInline", format, content]
        # content may include '<img', so check any string fields for '<img'
        for part in inline[1:]:
            if isinstance(part, str) and "<img" in part.lower():
                return True
    return False

def block_is_image_only(block):
    # block is like ["Para", [inlines...]] or ["Plain", [inlines...]] or ["RawBlock", fmt, content]
    if not isinstance(block, list) or len(block) == 0:
        return False
    tag = block[0]
    if tag in ("Para", "Plain"):
        inlines = block[1] if len(block) > 1 else []
        if not isinstance(inlines, list):
            return False
        # consider image-only if every non-space inline is Image or RawInline <img>
        for inline in inlines:
            if not is_image_inline(inline) and not (isinstance(inline, list) and inline[0] == "Space"):
                return False
        return True
    if tag == "RawBlock":
        # RawBlock: ["RawBlock", format, string]
        if len(block) >= 3 and isinstance(block[2], str) and "<img" in block[2].lower():
            return True
    return False

def block_is_text_paragraph(block):
    # paragraph-like block: Para or Plain and first non-space inline is textual (Str, Emph, Strong, Code, etc.)
    if not isinstance(block, list) or len(block) == 0:
        return False
    tag = block[0]
    if tag not in ("Para", "Plain"):
        return False
    inlines = block[1] if len(block) > 1 else []
    if not isinstance(inlines, list) or len(inlines) == 0:
        return False
    # find first non-space inline
    for inline in inlines:
        if isinstance(inline, list) and inline and inline[0] == "Space":
            continue
        if isinstance(inline, list) and inline:
            if inline[0] in ("Str", "Strong", "Emph", "Code", "Link", "Span"):
                return True
            # RawInline may contain text too — treat it as text
            if inline[0] == "RawInline":
                return True
    return False

def process_blocks(blocks):
    # blocks is a list of pandoc block arrays
    changed = True
    # We'll repeatedly scan and swap until no more swaps are made (handles consecutive image blocks)
    while True:
        swapped = False
        i = 0
        while i < len(blocks) - 1:
            b = blocks[i]
            nb = blocks[i+1]
            if block_is_image_only(b) and block_is_text_paragraph(nb):
                # swap: place nb then b
                blocks[i], blocks[i+1] = nb, b
                swapped = True
                # step back one position if possible to catch chained patterns
                i = max(i - 1, 0)
            else:
                i += 1
        if not swapped:
            break
    return blocks

def main(inp_path, out_path):
    with open(inp_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # pandoc JSON top-level may be an object with 'blocks' key (typical)
    if isinstance(data, dict) and "blocks" in data:
        blocks = data["blocks"]
        data["blocks"] = process_blocks(blocks)
    else:
        # If data is a raw list which is pandoc AST, try to find blocks
        # Some pandoc JSON outputs the whole AST as {"blocks":...} already; if not, attempt to find it.
        print("Unexpected JSON layout: expecting object with 'blocks' key.", file=sys.stderr)
        # fallback: treat top-level as blocks if it's a list
        if isinstance(data, list):
            data = process_blocks(data)
        else:
            print("Cannot process file: unknown pandoc JSON format.", file=sys.stderr)
            sys.exit(1)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: fix_pandoc_ast.py <in.json> <out.json>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
