import os

from file_parser import process_file
from html_parser import extract_text_from_url


def main():
    print("Choose an option to parse:")
    print("1. File")
    print("2. URL")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        file_path = input("Enter the path to the file: ")
        if os.path.exists(file_path):
            print(process_file(file_path))
        else:
            print("File not found.")
    elif choice == '2':
        url = input("Enter the URL: ")
        print(extract_text_from_url(url))
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
