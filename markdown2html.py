#!/usr/bin/python3
"""script that take 2 arguments:
1st:name of the Markdown file
2nd: the output file name
"""

import sys
import os.path


if len(sys.argv) <= 2:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    sys.exit(1)

if ".md" in sys.argv[1]:
    path = './'
    check_file = os.path.isfile(path + sys.argv[1])
    if not check_file:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
