# Text Parser

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/KordyD/data-analyser.git
   cd data-analyzer
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```sh
python main.py
```

Follow the prompts to choose between parsing a file or a URL.

## Docker

Build and run the Docker container:

```sh
docker-compose run --rm app
```

## Running Tests

To run the tests, use:

```sh
pytest
```

## File Parsing

The file parser supports the following formats:

- PDF
- DOCX
- HTML

Example usage:

```py
from parsers.file_parser import FileParser

parser = FileParser("path/to/file.pdf")
print(parser.process_file())
```

## URL Parsing

The URL parser fetches and extracts text from web pages.

Example usage:

```py
from parsers.web_parser import WebParser

parser = WebParser("https://www.example.com")
print(parser.process_url())
```
