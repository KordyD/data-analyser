import os
from bs4 import BeautifulSoup
import docx
import pymupdf

def process_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        return extract_text_from_docx(file_path)
    elif file_extension == '.html' or file_extension == '.htm':
        return extract_text_from_html(file_path)
    else:
        return "Unsupported file format."


def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error extracting text from DOCX: {e}"

def extract_text_from_pdf(file_path):
    try:
        doc = pymupdf.open(file_path)
        text = ''
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def extract_text_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            return text
    except Exception as e:
        return f"Error extracting text from HTML: {e}"
