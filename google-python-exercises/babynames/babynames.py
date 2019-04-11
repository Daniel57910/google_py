#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

def extract_names(filename):
	
	naming_data = []
	file_stream = open(filename, 'rU')

	for line in file_stream:
		data = re.findall(r'<td>(\w+)</td>', line)
		print data

	return


def main():
	# This command-line parsing code is provided.
	# Make a list of command line arguments, omitting the [0] element
	# which is the script itself.
	args = sys.argv[1:]

	if not args:
		print 'usage: [--summaryfile] file [file ...]'
		sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
	summary = False
	if args[0] == '--summaryfile':
		summary = True
		del args[0]

	extract_names(args[0])

if __name__ == '__main__':
	main()
