import os
from bs4 import BeautifulSoup
import docx
import pymupdf


class FileParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def process_file(self):
        _, file_extension = os.path.splitext(self.file_path)
        file_extension = file_extension.lower()

        if not os.path.exists(self.file_path):
            return "File not found."

        if file_extension == '.pdf':
            return self.__extract_text_from_pdf()
        elif file_extension == '.docx':
            return self.__extract_text_from_docx()
        elif file_extension == '.html' or file_extension == '.htm':
            return self.__extract_text_from_html()
        else:
            return "Unsupported file format."

    def __extract_text_from_docx(self):
        try:
            doc = docx.Document(self.file_path)
            text = '\n'.join([para.text for para in doc.paragraphs])
            return text
        except Exception as e:
            return f"Error extracting text from DOCX: {e}"

    def __extract_text_from_pdf(self):
        try:
            doc = pymupdf.open(self.file_path)
            text = ''
            for page in doc:
                text += page.get_text()
            return text
        except Exception as e:
            return f"Error extracting text from PDF: {e}"

    def __extract_text_from_html(self):
        try:
            file = self.__open_file()
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            return text
        except Exception as e:
            return f"Error extracting text from HTML: {e}"

    def __open_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Error opening file: {e}"
