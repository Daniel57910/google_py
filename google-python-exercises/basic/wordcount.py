#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
from collections import Counter

def increase_counter(w_counter, line):
	for word in line:
		w_counter[word.lower()] += 1
		
def print_words(file):
	word_counter = Counter()
	for line in file:
		line = line.split()
		increase_counter(word_counter, line)

	file.close()
	print word_counter.items()

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  file_stream = open(sys.argv[2], 'rU')

  if option == '--count':
    print_words(file_stream)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
