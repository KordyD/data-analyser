from parsers.web_parser import WebParser


def test_integration_with_real_url():
  url = "https://www.example.com"
  parser = WebParser(url)

  result = parser.process_url()
  assert "Example Domain" in result

def test_integration_with_real_url_failure():
  url = "https://www.example.com/nonexistent"
  parser = WebParser(url)

  result = parser.process_url()
  assert "Error fetching URL" in result