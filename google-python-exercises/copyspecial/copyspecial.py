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

def get_special_paths(path):

	files = os.listdir(path)
	special_files = []
	regex = r'(\w+)__(\w+)__.+([txt]|[jpg])'

	for file in files:
		if re.match(regex, file):
  			special_files.append(os.path.abspath(os.path.join(path, file)))

	return special_files

def to_zip(file_name, files):
	temp_dire = '/tmp/zipfiles'

	#create temporary directory and copy special files to directory
	to_directory(temp_dire, files)
	
	#zip the files using the file extension
	shutil.make_archive(file_name, 'zip', temp_dire)
	
	#finally delete the temp directory 
	try:
		shutil.rmtree(temp_dire)
	except OSerror as e:
		raise e


def make_directory(dire):

	try:
		os.makedirs(dire)
	except OSError:
		if not os.path.isdir(dire):
			raise


def to_directory(directory, files):
		make_directory(directory)
		for file in files:
			shutil.copy(file, directory)


def main():
	args = sys.argv[1:]
	if not args:
		print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
		sys.exit(1)

	if args[0] == '--todir':
		to_directory(args[1], get_special_paths(args[2]))

	if args[0] == '--tozip':
		to_zip(args[1], get_special_paths(args[2]))
		del args[0:2]		
	if len(args) == 0:
		print "error: must specify one or more dirs"
		sys.exit(1)		


if __name__ == "__main__":
	main()
