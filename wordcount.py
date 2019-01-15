#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(filename):
  dict_words = helper_function(filename)
  for key in sorted(dict_words):
    print("{} {}".format(key, dict_words[key]))


def print_top(filename):
  dict_words = helper_function(filename)
  top_20 = sorted(dict_words.items(), key=sort_dict, reverse=True)[:20]
  for i in top_20:
    print("{}".format(i[0]))


def sort_dict(key_value):
  return key_value[1]


def helper_function(filename):
  file_handler = open(filename, "r")
  dict_words = {}
  for lines in file_handler:
    lines = lines.lower()
    word_list = lines.split()
    for word in word_list:
      if (word not in dict_words):
        dict_words[word] = 1
      else:
        dict_words[word] += 1
  file_handler.close()
  return dict_words
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)


if __name__ == '__main__':
  main()
