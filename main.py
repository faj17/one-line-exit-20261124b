#!/usr/bin/env python3
"""The One-Line Exit entry.

Writes a single original funny one-line resignation letter to
/output/entry.txt (1-140 characters, UTF-8, a single line). Standard
library only, no network, no input.

The line is built from two fragments: a setup (a museum guard resigns
after three years guarding a painting of a man screaming) and a punch
(he has decided to join him). ``assemble`` joins them into the single
line; ``validate`` checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "I resign from the museum, effective today, because after three years guarding a painting of a man screaming,"
PUNCH = "I have decided to join him."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one resignation line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-140 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line must be 1-140 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
