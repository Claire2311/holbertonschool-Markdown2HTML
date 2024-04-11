#!/usr/bin/python3
"""Script to convert a Markdown file to HTML.

This script takes two arguments:
1. The name of the Markdown file to convert.
2. The name of the output HTML file.

Usage: python3 markdown2html.py input.md output.html
"""

import sys
import os.path
import re


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

    with open(sys.argv[1], 'r') as mdfile, open(sys.argv[2], 'a') as htmlfile:
        for line in mdfile:
            if line.startswith('#'):
                values = re.split(r'(^#+)\s', line.strip())
                title_level = str(len(values[1]))
                title = values[2].strip()
                final_title = ('<h' + title_level + '>' + 
                               title + '</h' + title_level + '>')
                htmlfile.write(final_title + '\n')

    with open(sys.argv[2], 'r') as f:
        data = f.read()
        with open(sys.argv[2], 'w') as w:
            w.write(data[:-1])


if __name__ == "__main__":
    main()
