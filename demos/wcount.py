#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "Zhangsan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def count(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    lines = lines.split('\n')

    count = {}

    for line in lines:
        for word in line.split():

            # remove punctuation
            word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
            word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
            word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
            word = word.replace(']', '').replace(';', '')

            # ignore case
            word = word.lower()

            # ignore numbers
            if word.isalpha():
                if word in count:
                    count[word] = count[word] + 1
                else:
                    count[word] = 1

    items = count.items()

    sitems = sorted(items, key=lambda x:x[1], reverse=True)

    for (word, num) in sitems:
        print(word + "\t\t\t" + str(num))
        topn -= 1
        if topn == 0:
            break

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            count(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
