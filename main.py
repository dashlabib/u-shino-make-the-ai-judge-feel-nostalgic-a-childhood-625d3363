#!/usr/bin/env python3
"""Write one childhood-memory sentence to /output/entry.txt and entry.txt.

Deterministic, stdlib only, no network. The entry is a single sentence,
at most 280 characters, recalling a specific childhood moment.
"""

import os

ENTRY = (
    "I used to save the last bite of my seventh birthday chocolate cake in "
    "my cheek "
    "until the chairs scraped back and the plates were cleared, because "
    "swallowing it meant the day was really over."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    assert text == text.strip(), "entry must not have surrounding whitespace"
    assert text.count(".") == 1 and text.endswith("."), "single sentence only"
    assert "\n" not in text, "no line breaks"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
