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

    sentences = []
    final_sentences = []

    with open(sys.argv[1], 'r') as mdfile, open(sys.argv[2], 'a') as htmlfile:
        for line in mdfile:
            sentences.append(line.strip())

        if sentences[-1] == '':
            sentences.pop()

        for num, sentence in enumerate(sentences):
            if sentences[num].startswith('#'):
                final_sentences.append(sentences[num])

            if sentences[num].startswith('-') and \
                    not sentences[num-1].startswith('-'):
                final_sentences.append("<ul>")
                final_sentences.append(sentences[num])

            if sentences[num].startswith('-') and \
                    not sentences[num+1].startswith('-'):
                final_sentences.append(sentences[num])
                final_sentences.append("</ul>")

            if sentences[num].startswith('-') and \
                    sentences[num+1].startswith('-') and \
                    sentences[num-1].startswith('-'):
                final_sentences.append(sentences[num])

            if re.match("^[a-zA-Z]+", sentences[num]) and \
                    not re.match("^[a-zA-Z]+", sentences[num-1]):
                final_sentences.append("<p>")
                final_sentences.append(sentences[num])

            if re.match("^[a-zA-Z]+", sentences[num]) and \
                    re.match("^[a-zA-Z]+", sentences[num-1]):
                final_sentences.append("<br />")
                final_sentences.append(sentences[num])

            if re.match("^[a-zA-Z]+", sentences[num]) and \
                    (num == len(sentences)-1 or sentences[num+1] == ""):
                final_sentences.append("</p>")

        for num, sentence in enumerate(final_sentences):
            if sentence.startswith('#'):
                values = re.split(r'(^#+)\s', sentence.strip())
                title_level = str(len(values[1]))
                title = values[2].strip()
                final_sentences[num] = ('<h' + title_level + '>' +
                                        title + '</h' + title_level + '>')

            if sentence.startswith('-'):
                unordered_list_elem = re.split(r'(^-)\s', sentence.strip())[2]
                final_sentences[num] = '<li>' + unordered_list_elem + '</li>'

            if sentence.startswith('*'):
                ordered_list_elem = sentence.split('* ')[1]
                final_sentences[num] = '<li>' + ordered_list_elem + '</li>'

        for num, sentence in enumerate(final_sentences):
            if "**" in sentence:
                final_sentences[num] = sentence.replace("**", "</b>")\
                    .replace("</b>", "<b>", 1)

            if "__" in sentence:
                final_sentences[num] = sentence.replace("__", "</em>")\
                    .replace("</em>", "<em>", 1)

        htmlfile.writelines(line + '\n' for line in final_sentences)

    with open(sys.argv[2], 'r') as f:
        data = f.read()
        with open(sys.argv[2], 'w') as w:
            w.write(data[:-1])


if __name__ == "__main__":
    main()
