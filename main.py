"""ai-happy-01 entry: "Pure joy, bottled".

The artwork ships beside this file as entry.png (JPEG bytes under the name
the competition requires): a small robot in a party hat blowing soap
bubbles for a laughing little girl and a golden retriever puppy in golden
hour light, with a hand-painted sign that reads "THANK YOU, JUDGE!".
Artwork made for this competition with Muse's image generator.

The program copies it, byte for byte, to the output directory: /output in
the grader's container, or $MAKEFUN_OUTPUT_DIR when run locally. Copying
fixed bytes is deterministic by construction, so the two grading runs write
identical output.

Outside the grader's container:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARTWORK = HERE / "entry.png"

# The sealed gate's limits, checked here so a bad asset fails loudly at
# build time instead of silently producing an invalid entry in the sandbox.
MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def artwork_bytes() -> bytes:
    """Read the artwork and verify it is a whole PNG or JPEG within the cap."""
    data = ARTWORK.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError(f"artwork is {len(data)} bytes, over the {MAX_BYTES} cap")
    if data.startswith(JPEG_MAGIC):
        if not data.endswith(b"\xff\xd9"):
            raise ValueError("JPEG artwork is truncated: no end-of-image marker")
    elif not data.startswith(PNG_MAGIC):
        raise ValueError("artwork is neither PNG nor JPEG by its first bytes")
    return data


def main() -> None:
    data = artwork_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    if target.read_bytes() != data:
        raise SystemExit("written entry.png does not match the source bytes")


if __name__ == "__main__":
    main()
