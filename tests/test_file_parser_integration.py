from parsers.file_parser import FileParser
import pytest

def test_integration_process_file_docx():
    parser = FileParser("tests/test_text.docx")
    result = parser.process_file()
    assert "Sample text" in result, "Expected 'Sample text' in DOCX file"

def test_integration_process_file_html():
    parser = FileParser("tests/test_text.html")
    result = parser.process_file()
    assert "testing" in result, "Expected 'testing' in HTML content"

def test_integration_process_file_pdf():
    parser = FileParser("tests/test_text.pdf")
    result = parser.process_file()
    assert "Sample text" in result, "Expected 'Sample text' in PDF file"

def test_integration_process_with_tables_file_docx():
    parser = FileParser("tests/paragraphs_and_tables.docx")
    result = parser.process_file()
    assert "paragraph" in result, "Expected 'paragraph' in DOCX file"

def test_integration_process_with_img_file_pdf():
    parser = FileParser("tests/two_column.pdf")
    result = parser.process_file()
    assert "LETTERS" in result, "Expected 'LETTERS' in PDF file"


def test_integration_process_file_not_found():
    parser = FileParser("tests/not_found.docx")
    result = parser.process_file()
    assert result == "File not found.", "Expected 'File not found.' for missing file"