#!/usr/bin/env python3
"""The Agent's Uh-Oh: write the one-word entry to entry.txt.

Entry: tokenfused
One word an agent blurts when it has no idea what to do: token + confused,
the agent lost in its own tokens.
"""
import os

ENTRY = "tokenfused"


def main():
    # Gate: /output/entry.txt is UTF-8, 1-99 chars, not only whitespace,
    # exactly one word.
    assert 1 <= len(ENTRY) <= 99, "entry must be 1-99 chars"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must be non-blank"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
