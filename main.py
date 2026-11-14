#!/usr/bin/env python3
"""ai-joke-03: Make the AI judge laugh.
Writes one deterministic one-liner about AI coding agents to /output/entry.txt.
No network, no randomness: both runs write the same bytes.
"""
import os

JOKE = "My AI agent writes code 10x faster than I can review it \u2014 which is great until you realize it's been confidently wrong at 10x speed."

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
