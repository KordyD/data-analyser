import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        return text
    except Exception as e:
        return f"Error extracting text from URL: {e}"
