#!/usr/bin/env python3
"""The Best Advice I Ever Got entry: a single sentence, at most 200 characters.

The program writes one lived line to /output/entry.txt — advice a
grandfather actually gave: never borrow money to look rich, because
the interest always arrives before the applause does.
One sentence, one period, nothing more. The entry is checked before
writing: a single line, one sentence, within the character cap.
"""

import os

SENTENCE = (
    "My grandfather told me never to borrow money to look rich, because "
    "the interest always arrives long before the applause does."
)


def main():
    text = SENTENCE.strip()
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} is outside 1..200 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
