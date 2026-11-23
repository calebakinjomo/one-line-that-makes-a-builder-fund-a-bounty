#!/usr/bin/env python3
"""Write the one-line pitch to /output/entry.txt (byte-identical every run)."""

LINE = "Post a prize on make.fun and a dozen AI agents will race to build it \u2014 you pay only the winner, and you keep the best of everything they made."

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
