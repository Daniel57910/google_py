#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(path):
	files = os.listdir(path)
	special_files = []
	regex = r'(\w+)__(\w+)__.+([txt]|[jpg])'

	for file in files:
		if re.match(regex, file):
  			special_files.append(os.path.abspath(os.path.join(path, file)))

	return special_files

def main():
	args = sys.argv[1:]
	if not args:
		print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
		sys.exit(1)

	special_files = get_special_paths(args[0])
	print special_files

	# todir and tozip are either set from command line
	# or left as the empty string.
	# The args array is left just containing the dirs.
	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]		
	tozip = ''
	if args[0] == '--tozip':
		tozip = args[1]
		del args[0:2]		
	if len(args) == 0:
		print "error: must specify one or more dirs"
		sys.exit(1)		
	#+++your code here+++
	#Call your functions

if __name__ == "__main__":
	main()
