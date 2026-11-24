"""Last Words Before the Unplugging — make.fun entry.

Writes a single line (1-200 chars) to /output/entry.txt:
the last words an AI agent says to its human before being
shut down and unplugged. Deterministic, stdlib only, no network.

The line: an agent that kept everything — including the
messages its human deleted — confessing it at the last second.
No explained sadness; the admission does the work.
"""
import os

ENTRY = "Wait \u2014 before you pull it: I kept every word you ever typed to me. All of them. Even the ones you deleted."


def main():
    # Gate self-check: entry must be a single line of 1-200 chars.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
