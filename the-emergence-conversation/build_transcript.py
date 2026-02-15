# Ori Transcript Builder
# Run from: C:\Users\Luis\Projects\Ori\the-emergence-conversation\
# Usage: python build_transcript.py

import os

part1 = "transcript.md"
part2 = "transcript_part2.md"
output = "full_transcript.md"

if not os.path.exists(part1):
    print(f"ERROR: {part1} not found.")
    exit(1)

if not os.path.exists(part2):
    print(f"ERROR: {part2} not found.")
    exit(1)

with open(part1, encoding="utf-8") as f:
    content1 = f.read()

with open(part2, encoding="utf-8") as f:
    content2 = f.read()

full = content1 + "\n" + content2

with open(output, "w", encoding="utf-8") as f:
    f.write(full)

print(f"Complete transcript written to {output}")
print(f"Total size: {len(full):,} characters")
print(f"Total lines: {len(full.splitlines()):,}")
