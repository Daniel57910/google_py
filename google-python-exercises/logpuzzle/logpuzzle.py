#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

def read_urls(filename, file_type):

	special_files = []
	keyword = 'puzzle'
	server_name = 'http://code.google.com'	
	for file in filename:
		url = file.partition('"GET ')[2].rpartition("HTTP")[0]
		if (keyword in url) and (server_name + url) not in special_files: 
			special_files.append(server_name + url)

	if file_type == 'animal': return sorted(special_files)
	if file_type == 'place': return sorted(special_files, key=sort_by_middle_word)

def sort_by_middle_word(word):
	return re.search(r'\p-(\w+)-(\w+)', word).group(2)

def make_directory(directory):

	print('making directory')
	try:
		os.makedirs(directory)
	except OSError:
		if not os.path.isdir(directory):
			raise

def download_images(img_urls, dest_dir):

	img_name = dest_dir + '/img_'
	img_list = []
	count = 0
	make_directory(dest_dir)

	print('Retrieving URLs')
	for img in img_urls:

		if not os.path.exists(img_name + str(count)):
			urllib.urlretrieve(img, img_name + str(count))
			
		count+=1
		img_list.append(img_name + str(count))

	return img_list

def create_html_file(img_list, html_file):
	open_tag = '<img src=" '
	close_tag = '">'
	file = open(html_file, 'w+')
	
	for image in img_list:
		image_for_file = open_tag + image + close_tag
		file.write(image_for_file)
	
	file.close()




def main():

	args = sys.argv[1:]
	dest_dir = os.getcwd() + '/' + 'images'
	animal_html_file = os.getcwd() + '/' + 'animal_index.html'
	place_html_file = os.getcwd() + '/' + 'place_index.html'

	if not args:
		print('usage: [--todir dir] logfile ')
		sys.exit(1)

	if args[0] == '--todir':
		if 'animal' in args[1]:	create_html_file(download_images(read_urls(open(args[2], 'rU'), 'animal'), args[1]), animal_html_file)
		if 'place' in args[1]:	create_html_file(download_images(read_urls(open(args[2], 'rU'), 'place'), args[1]), place_html_file)
	else:
		print("\n".join(read_urls(open(args[0], 'rU'))))


if __name__ == '__main__':
  main()
