#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

def extract_names(filename):
	
	naming_data = {}
	file_stream = open(filename, 'rU')

	for line in file_stream:
		data = re.findall(r'<td>(\w+)</td>', line)
		if (len(data) == 3):
			naming_data[data[1]] = data[0]
			naming_data[data[2]] = data[0]

	file_stream.close()
	return naming_data

def report_summary(filename, file_year, names):
	open_stream = open(filename+'.summary', 'w+')
	open_stream.write('%s\n' %file_year)

	for name in names:
		open_stream.write('%s: %s\n' %(name[0], name[1]))

	open_stream.close()

def console_print(file_year, names):
	print file_year
	for name in names:
		print '%s: %s' %(name[0], name[1])

def return_data(names, filename, summary):

	file_year = ''.join(re.findall(r'(\d+)', filename))

	if summary == False:
		console_print(file_year, names)
	else:
		report_summary(filename, file_year, names)
	

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

	name_data = extract_names(args[0])
	return_data(sorted(name_data.items()), args[0], summary)

if __name__ == '__main__':
	main()


