import os
from pathlib import Path

def remove_redundant_images(content_dir):
    for root, _, files in os.walk(content_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in ['.jpeg', '.jpg', '.png']:
                if not check_references(file_path):
                    file_path.unlink()
                    print(f"Deleted: {file_path}")

def check_references(file_path):
    md_files = list(Path(file_path.parent).glob("*.md"))
    for md_file in md_files:
        if file_path.name in md_file.read_text():
            return True
    return False

remove_redundant_images("content")