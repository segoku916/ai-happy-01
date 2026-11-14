#!/usr/bin/env python3
"""ai-happy-01 entry: copy the entry image to the grader's output directory.

The image beside this file (entry.png) is the entry: a golden retriever
puppy mid-leap, catching a big iridescent soap bubble on its nose in a
sunlit garden. The program does one thing: copy those exact bytes to
/output/entry.png, so the judge sees precisely the image the repository
holds. A pure byte copy is deterministic: two runs write identical bytes.

Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise SystemExit(f"entry image not found: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("copy incomplete: size mismatch")


if __name__ == "__main__":
    main()
