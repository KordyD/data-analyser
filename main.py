import os

from parsers import web_parser, file_parser


def main():
    print("Choose an option to parse:")
    print("1. File")
    print("2. URL")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        file_path = input("Enter the path to the file: ")
        parser = file_parser.FileParser(file_path)
        print(parser.process_file())
    elif choice == '2':
        url = input("Enter the URL: ")
        parser = web_parser.WebParser(url)
        print(parser.process_url())
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
