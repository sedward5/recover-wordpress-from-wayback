import requests
from bs4 import BeautifulSoup
from pathlib import Path

def fetch_and_save_page(url, save_dir):
    """Fetches a webpage and saves its content to a local file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'class': 'entry-content'})  # Adjust based on your site's structure
        if content:
            save_dir.mkdir(parents=True, exist_ok=True)
            (save_dir / "index.html").write_text(str(content))
            print(f"Saved: {save_dir / 'index.html'}")
        else:
            print(f"No content found for {url}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# Example usage
urls = ["https://web.archive.org/web/example-page"]
save_dir = Path("content")
for url in urls:
    fetch_and_save_page(url, save_dir / Path(url.split('/')[-1]))