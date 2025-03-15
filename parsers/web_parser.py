import requests
from bs4 import BeautifulSoup

class WebParser:

    def __init__(self, url):
        self.url = url

    def __fetch_url(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response
        except Exception as e:
            return f"Error fetching URL: {e}"

    def __extract_text(self, content):
        try:
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            return text
        except Exception as e:
            return f"Error extracting text: {e}"

    def process_url(self):
        response = self.__fetch_url()
        # if err
        if isinstance(response, str):
            return response
        return self.__extract_text(response.content)