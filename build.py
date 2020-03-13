import os
from pathlib import Path
import markdown

OUTPUT_FOLDER = os.path.join(os.getcwd(), "build")
INPUT_FOLDER = os.path.join(os.getcwd(), "docs")

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

if not os.path.exists(INPUT_FOLDER):
    os.mkdir(INPUT_FOLDER)

with os.scandir(INPUT_FOLDER) as entries:
    for entry in entries:
        if entry.is_file():
            output_filename = f"{Path(entry.name).stem}.html"
            html = markdown.markdownFromFile(
                input=entry.path, output=os.path.join(OUTPUT_FOLDER, output_filename),
                encoding="UTF-8"
            )
