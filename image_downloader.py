import requests
from pathlib import Path

def download_image(url, save_path):
    """Downloads an image from a URL and saves it locally."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {save_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Example usage
image_urls = ["https://cdn.example.com/image1.jpg"]
save_dir = Path("images")
save_dir.mkdir(exist_ok=True)
for url in image_urls:
    download_image(url, save_dir / Path(url.split('/')[-1]))