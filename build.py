import os
import markdown

OUTPUT_FOLDER = os.path.join(os.getcwd(), "build")

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

html = markdown.markdownFromFile(
    input="docs.md", output=os.path.join(OUTPUT_FOLDER, "docs.html"), encoding="UTF-8"
)
