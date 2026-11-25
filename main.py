"""Ship the finished news image.

The image itself (``entry.png``) is produced by ``gen_image.py`` and is
already final. This entry point only copies it into the directory the
platform asks for, using the standard library only.

Usage:
    MAKEFUN_OUTPUT_DIR=/path/to/out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"copied {SOURCE} -> {target}")


if __name__ == "__main__":
    main()
