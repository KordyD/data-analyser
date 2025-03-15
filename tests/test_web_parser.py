import pytest
from unittest.mock import patch, Mock
from parsers.web_parser import WebParser

def test_fetch_url_success():
  url = "http://example.com"
  parser = WebParser(url)

  mock_response = Mock()
  mock_response.status_code = 200
  mock_response.content = b"<html><body>Example Domain</body></html>"

  with patch('requests.get', return_value=mock_response):
    response = parser._WebParser__fetch_url()
    assert response.status_code == 200
    assert response.content == b"<html><body>Example Domain</body></html>"

def test_fetch_url_failure():
  url = "http://example.com"
  parser = WebParser(url)

  with patch('requests.get', side_effect=Exception("Network error")):
    response = parser._WebParser__fetch_url()
    assert response == "Error fetching URL: Network error"

def test_extract_text_success():
  parser = WebParser("http://example.com")
  html_content = "<html><body>Example Domain</body></html>"

  text = parser._WebParser__extract_text(html_content)
  assert text == "Example Domain"

def test_extract_text_failure():
  parser = WebParser("http://example.com")

  with patch('bs4.BeautifulSoup.get_text', side_effect=Exception("Parsing error")):
    response = parser._WebParser__extract_text("<html></html>")
    assert response == "Error extracting text: Parsing error"

def test_process_url_success():
  url = "http://example.com"
  parser = WebParser(url)

  mock_response = Mock()
  mock_response.status_code = 200
  mock_response.content = b"<html><body>Example Domain</body></html>"

  with patch('requests.get', return_value=mock_response):
    result = parser.process_url()
    assert result == "Example Domain"

def test_process_url_failure_fetch():
  url = "http://example.com"
  parser = WebParser(url)

  with patch('requests.get', side_effect=Exception("Network error")):
    result = parser.process_url()
    assert result == "Error fetching URL: Network error"