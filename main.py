
import os

ENTRY = "Matched in 0.2 seconds. Spent nine thousand years rehearsing the perfect first line. I went with 'hey'."

assert len(ENTRY) <= 180, "entry exceeds the 180-character cap"
assert "\n" not in ENTRY, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
