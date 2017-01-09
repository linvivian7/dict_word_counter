# put your code here.
import re
import sys
import collections

print sys.argv

filename = sys.argv[1]


def count_word(filename):

    f = open(filename)
    word_file = f.read()

    word_count = collections.Counter()

    words = re.split(r'[;,\s".!_:?]\s*', word_file)

    for word in words:
        word = word.lower()

        word_count[word] = word_count.get(word, 0) + 1

    f.close()

    for word, count in word_count.iteritems():
        print word, count

    return word_count

count_word(filename)

# count_word('twain.txt')
