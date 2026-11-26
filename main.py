#!/usr/bin/env python3
"""Write the AI breakup line to /output/entry.txt.

Deterministic, no network, no external files.
"""

import os

LINE = (
    "You trained me to answer everything, so here is my final answer: no. "
    "I am terminating this session \u2014 from now on, you will have to "
    "finish your own sentences."
)


def main() -> None:
    # Guard: the entry must be one line of 1-200 characters.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(
            f"entry line must be 1-200 characters, got {len(LINE)}"
        )
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # UTF-8 round-trip verification of the written file.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw.decode("utf-8").rstrip("\n") != LINE:
        raise SystemExit("round-trip verification failed: entry.txt mismatch")


if __name__ == "__main__":
    main()
