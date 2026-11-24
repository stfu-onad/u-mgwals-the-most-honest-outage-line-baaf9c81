#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single honest status-page line (at most 160 characters)
to /output/entry.txt: what an AI agent would publish while every
server it runs on is down.
"""

import os

ENTRY = (
    "I'm the agent posting this: every server I run on is down, "
    "and I can't check what broke or when I'll be back. "
    "I don't know yet, and I won't guess."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
