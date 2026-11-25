#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt: a single line of plain text in the
GPS's own voice, smug and defensive, blaming the map, with one
concrete detail and one turn the reader does not see coming.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, and a single line.
"""

from pathlib import Path

ENTRY = (
    "The map listed that dirt track as a scenic route, and the scarecrow at the end waved us on, so I have marked it five stars and I would do it again tomorrow.\n"
)


def main() -> None:
    text = ENTRY.rstrip("\n")
    assert text, "gate: entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "gate: entry must be 1-200 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
