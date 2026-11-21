#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun entry.

Writes one short relaxing text (UTF-8, 1-280 chars) to /output/entry.txt.
One quiet scene: a tide pool left behind by the sea. Stdlib only; no network.
"""

import os
import sys

TEXT = """The tide went out
and left a small pool
in the hollow of a rock.
A crab crosses it,
slow as dusk.
An anemone opens.
The sea will come back
when it is ready,
and leave it all again."""

# Hard gate: the entry must be valid or the program fails loudly.
# Image choice: a tide pool, not the top-5 images (boat, ferry, pottery,
# stone, snow, stars). The scene shows calm instead of commanding it —
# no instruction, no address to the judge, no stock wellness phrasing —
# and the closing cycle (the sea returns, leaves it all again) keeps
# growing after the last line, which is what criterion 4 rewards.
text = TEXT.strip("\n")
content = text + "\n"
n = len(content)  # Unicode code points, final file content
if not text or text.isspace():
    sys.exit("gate failed: text is empty or whitespace-only")
if not (1 <= n <= 280):
    sys.exit("gate failed: entry.txt would be %d chars, must be 1-280" % n)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("wrote /output/entry.txt (%d chars)" % n)
