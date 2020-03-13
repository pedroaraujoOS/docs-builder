import os
import sys
from pathlib import Path

import markdown

OUTPUT_FOLDER = os.path.join(os.getcwd(), "build")
INPUT_FOLDER = os.path.join(os.getcwd(), "docs")

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

if not os.path.exists(INPUT_FOLDER):
    print(f"{INPUT_FOLDER} does not exist")
    sys.exit(1)

with os.scandir(INPUT_FOLDER) as entries:
    i = 0
    for entry in entries:
        if not entry.is_file():
            continue
        output_filename = f"{Path(entry.name).stem}.html"
        html = markdown.markdownFromFile(
            input=entry.path, output=os.path.join(OUTPUT_FOLDER, output_filename),
            encoding="UTF-8"
        )
        i += 1

if i == 0:
    print("No files processed")
    sys.exit(1)

