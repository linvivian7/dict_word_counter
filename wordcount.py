# put your code here.
import re
import sys

print sys.argv

filename = sys.argv[1]


def count_word(filename):
    word_file = open(filename)

    word_count = {}

    for line in word_file:

        words = re.split(r'[;,\s".!_:?]\s*', line.rstrip())

        for word in words:
            word = word.lower()

            word_count[word] = word_count.get(word, 0) + 1

    word_file.close()

    for word, count in word_count.iteritems():
        print word, count

    return word_count

count_word(filename)

# count_word('twain.txt')
