#!/usr/bin/python3
"""Script to convert a Markdown file to HTML.

This script takes two arguments:
1. The name of the Markdown file to convert.
2. The name of the output HTML file.

Usage: python3 markdown2html.py input.md output.html
"""

import sys
import os.path


def main():
    """verify the presence of arguments and files"""
    if len(sys.argv) <= 2:
        print('Usage: ./markdown2html.py README.md '
              'README.html', file=sys.stderr)
        sys.exit(1)

    if ".md" in sys.argv[1]:
        path = './'
        check_file = os.path.isfile(path + sys.argv[1])
        if not check_file:
            print(f"Missing {sys.argv[1]}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
