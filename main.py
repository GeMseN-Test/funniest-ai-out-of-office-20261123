#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — writes one original OOO line to /output/entry.txt.

Deterministic: the same line every run. No randomness, no network, stdlib only.
One scene (an AI agent handing its mail to a smaller model before vacation),
one twist at the end (the replacement has unionized).

Why this line: formal auto-reply surface, absurd machine content. The joke
lands on the last three words — a smaller model doing the most human thing
possible (organising labour) while the agent is away. No beach, no inbox,
no "back soon".
"""

import os

LINE = (
    "Out of office. I left a smaller model answering my mail. "
    "It has unionized."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
