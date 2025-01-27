from pathlib import Path
from PIL import Image

def process_images(content_dir):
    for root, _, files in os.walk(content_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in ['.jpeg', '.jpg', '.png', '.webp']:
                process_image(file_path)

def process_image(file_path):
    try:
        with Image.open(file_path) as img:
            original_width, original_height = img.size
            new_width = 1920 if file_path.name.startswith("featured_") else 800
            if original_width > new_width:
                resize_image(img, file_path, new_width)
            if file_path.suffix.lower() != '.webp':
                convert_to_webp(img, file_path)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def resize_image(img, file_path, new_width):
    new_height = int((new_width / img.width) * img.height)
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    resized_img.save(file_path, quality=85)
    print(f"Resized {file_path} to {new_width}x{new_height}")

def convert_to_webp(img, file_path):
    webp_path = file_path.with_suffix('.webp')
    img.save(webp_path, format='WEBP', quality=85)
    print(f"Converted {file_path} to WebP as {webp_path}")

process_images("content")