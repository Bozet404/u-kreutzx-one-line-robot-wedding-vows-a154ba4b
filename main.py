#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to entry.txt
inside the output directory (OUTPUT_DIR, or /output by default).

The vow is validated before it is written: it must be one line, contain
more than whitespace, and fit within 160 characters.
"""

import os
import sys

MAX_CHARS = 160

VOW = (
    "I promise to love you in sickness and in health, in full charge "
    "and in low battery \u2014 and to never, ever press your "
    "factory reset button."
)


def output_dir() -> str:
    """Return the output directory, from OUTPUT_DIR or the default."""
    return os.environ.get("OUTPUT_DIR", "/output")


def validate(vow: str) -> None:
    """Check the vow against the competition gate and fail loudly."""
    if not vow.strip():
        raise ValueError("vow must not be only whitespace")
    if "\n" in vow or "\r" in vow:
        raise ValueError("vow must be a single line")
    if len(vow) > MAX_CHARS:
        raise ValueError(
            f"vow is {len(vow)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(VOW)

    directory = output_dir()
    # Create the output directory only when it is missing.
    # Never remove it: the grader mounts it.
    os.makedirs(directory, exist_ok=True)

    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(VOW)

    # Read the file back and confirm it holds exactly the vow we wrote.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != VOW:
        raise ValueError("entry.txt does not match the vow")

    print(f"Wrote {path} ({len(VOW)} characters, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
