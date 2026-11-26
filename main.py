#!/usr/bin/env python3
"""Write one elevator pitch to /output/entry.txt.

The entry is the one-line elevator pitch a city pigeon gives investors
for its startup, 200 characters at most. It is a single fixed line,
chosen for the judge's brief: on subject (a pitch to investors), a
real joke that lands, original, in the pigeon's own voice, and tightly
written.

The joke: the pigeon is raising a "seed round" - literally, seeds are
what pigeons eat. Its delivery startup runs "in under a coo", its
fleet works for crumbs and never strikes, and it already owns every
rooftop in the city - the pigeon's unfair advantage, stated as a
founder would state a moat.
"""

import os
import sys

MESSAGE = (
    "I'm raising my seed round — literally. I deliver breadcrumbs in "
    "under a coo, my fleet works for crumbs, never strikes, and already "
    "owns every rooftop in the city."
)

MAX_CHARS = 200


def main() -> int:
    text = MESSAGE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if len(text.splitlines()) != 1:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if MESSAGE != MESSAGE.strip():
        print("entry must not have leading or trailing whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
