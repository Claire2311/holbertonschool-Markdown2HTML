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
    # """verify the presence of arguments and files"""
    # if len(sys.argv) <= 2:
    #     print('Usage: ./markdown2html.py README.md '
    #           'README.html', file=sys.stderr)
    #     sys.exit(1)

    if ".md" in sys.argv[1]:
        path = './'
        check_file = os.path.isfile(path + sys.argv[1])
        if not check_file:
            print(f"Missing {sys.argv[1]}", file=sys.stderr)
            sys.exit(1)

    sentences = []
    unordered_list = []
    ordered_list = []
    final_sentences = []

    with open(sys.argv[1], 'r') as mdfile, open(sys.argv[2], 'a') as htmlfile:
        for line in mdfile:
            sentences.append(line.strip())

        if sentences[-1] == '':
            sentences.pop()

        for num, sentence in enumerate(sentences, 1):
            if sentence.startswith('-'):
                unordered_list.append(num)

            if sentence.startswith('*'):
                ordered_list.append(num)

        if unordered_list:
            second_ul = unordered_list[-1]
            first_ul = unordered_list[0] - 1
            sentences.insert(second_ul, '</ul>')
            sentences.insert(first_ul, '<ol>')

        if ordered_list:
            second_ol = ordered_list[-1]
            first_ol = ordered_list[0] - 1
            sentences.insert(second_ol, '</ol>')
            sentences.insert(first_ol, '<ol>')

        final_sentences = sentences

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

        htmlfile.writelines(line + '\n' for line in final_sentences)

    with open(sys.argv[2], 'r') as f:
        data = f.read()
        with open(sys.argv[2], 'w') as w:
            w.write(data[:-1])


if __name__ == "__main__":
    main()
