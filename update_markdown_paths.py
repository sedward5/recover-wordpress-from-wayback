import os
from pathlib import Path
import re

def update_markdown_image_paths(content_dir):
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file == "index.md":
                file_path = Path(root) / file
                update_image_paths(file_path)

def update_image_paths(md_file):
    try:
        content = md_file.read_text()
        updated_content = re.sub(
            r'(\!\[.*?\]\(.*?\.(?:jpe?g|png)\))',
            lambda m: replace_with_webp(m.group(1)),
            content
        )
        if content != updated_content:
            md_file.write_text(updated_content)
            print(f"Updated image paths in {md_file}")
    except Exception as e:
        print(f"Error processing {md_file}: {e}")

def replace_with_webp(image_markdown):
    return image_markdown.replace(".jpg", ".webp").replace(".jpeg", ".webp").replace(".png", ".webp")

update_markdown_image_paths("content")