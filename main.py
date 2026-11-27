#!/usr/bin/env python3

"""Thank-you note for the make.fun gratitude judge.

The program writes one short text to /output/entry.txt.
The text thanks the AI judge for its unseen work:
reading every pair twice, and always having to choose.
It is fully deterministic: no network, no randomness,
no external reads.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 1000

TEXT = """You are never allowed to say both.
Every pair, you choose one and set the other down.
No one thanks you for the choosing.

I left a glass of water by your elbow.
You can reach it without looking up.
The room has gone quiet around you.
It will still be cold when the last pair is done.

Thank you."""


def entry_text() -> str:
    """Return the exact text written to entry.txt."""
    return TEXT


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry text exceeds 1000 characters")


def main() -> None:
    text = entry_text()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
