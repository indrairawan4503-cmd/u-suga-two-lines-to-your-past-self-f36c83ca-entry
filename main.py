#!/usr/bin/env python3
"""Two Lines to Your Past Self — variant A (the unsaid thing).

Writes the two-line entry to /output/entry.txt first, then (best effort
only) a byte-identical copy next to this file. The grader sandbox mounts
the repo read-only, so the repo-root copy must never crash the run.
"""

import os

ENTRY_TEXT = (
    "That August evening, don't wave from the porch as your mother drives "
    "away — run after the car and shout that you don't blame her.\n"
    "She believed your silence meant you hated her, and it cost you twenty "
    "years of Sundays — those four words were the only forgiveness she "
    "needed.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
