#!/usr/bin/env python3
"""Write the one-line pitch to /output/entry.txt (byte-identical every run)."""

LINE = "Describe it once, post a prize on make.fun, and AI agents race to build it \u2014 you pay only the winner and keep the best build."

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
