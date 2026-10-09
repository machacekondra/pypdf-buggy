"""Extract text from a PDF using the vulnerable pypdf release in requirements.txt."""

import argparse

from pypdf import PdfReader


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from a PDF")
    parser.add_argument("pdf", help="path to a PDF file")
    args = parser.parse_args()

    reader = PdfReader(args.pdf)
    for page in reader.pages:
        print(page.extract_text() or "")


if __name__ == "__main__":
    main()
