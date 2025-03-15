import pytest
from unittest.mock import patch, mock_open
from parsers.file_parser import FileParser

def test_process_file_pdf():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.pdf")
        with patch.object(FileParser, '_FileParser__extract_text_from_pdf', return_value="PDF content"):
            result = parser.process_file()
            assert result == "PDF content"

def test_process_file_docx():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.docx")
        with patch.object(FileParser, '_FileParser__extract_text_from_docx', return_value="DOCX content"):
            result = parser.process_file()
            assert result == "DOCX content"

def test_process_file_html():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.html")
        with patch.object(FileParser, '_FileParser__extract_text_from_html', return_value="HTML content"):
            result = parser.process_file()
            assert result == "HTML content"

def test_process_file_unsupported():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.txt")
        result = parser.process_file()
        assert result == "Unsupported file format."

def test_extract_text_from_docx():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.docx")
        with patch("docx.Document") as mock_doc:
            mock_doc.return_value.paragraphs = [type('obj', (object,), {'text': 'Paragraph 1'})]
            result = parser._FileParser__extract_text_from_docx()
            assert result == "Paragraph 1"

def test_extract_text_from_pdf():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.pdf")
        with patch("pymupdf.open") as mock_pdf:
            mock_pdf.return_value = [type('obj', (object,), {'get_text': lambda: 'Page 1'})]
            result = parser._FileParser__extract_text_from_pdf()
            assert result == "Page 1"

def test_extract_text_from_html():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.html")
        mock_html_content = "<html><body><p>Paragraph 1</p></body></html>"
        with patch("builtins.open", mock_open(read_data=mock_html_content)):
            with patch("parsers.file_parser.BeautifulSoup") as mock_soup:
                mock_soup.return_value.get_text.return_value = "Paragraph 1"
                result = parser._FileParser__extract_text_from_html()
                assert result == "Paragraph 1"

def test_open_file():
    with patch("os.path.exists", return_value=True):
        parser = FileParser("test.html")
        mock_file_content = "File content"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = parser._FileParser__open_file()
            assert result == "File content"