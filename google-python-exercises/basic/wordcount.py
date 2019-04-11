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
		word = ''.join(list(filter(lambda char: (char.isalnum()), word)))
		if word != '' and word[0].isalpha(): 
			w_counter[word.lower()] += 1
	
def print_pretty(words, count):
	print 'hello'
	for i in range(count):
		print '%s: %s' %(words[i][0], words[i][1])

def main():

  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  file_stream = open(sys.argv[2], 'rU')
  word_counter = Counter()

  for line in file_stream:
  	increase_counter(word_counter, line.split())

  file_stream.close()

  if option == '--count':
	  print_pretty(sorted(word_counter.items()), len(word_counter))
  elif option == '--topcount':
	  print_pretty(sorted(word_counter.items()), 20)
  else:
    print 'unknown option: ' + option
    sys.exit(1)


if __name__ == '__main__':
	main()
