'''
File : editwebsite.py
Author : Greg Furlich
Date Created : 9/17/2017

Purpose : Create a toolbox of functions to read, view, and modify html pages and tags.


'''

# Python Libraries	
import urllib
import re
import os
import sys
import time
import subprocess

#--- Python Functions for Manipulating HTML Pages and Tags ---#

# Read page html code into array :
def readPage( infile):
	'''
	Reads in HTML code from infile into list by line
	'''

	page = urllib.urlopen(infile).read()
	try:
		page = re.split('\n',page)
		return page

	except ValueError:
        	return 'Uable to Read Page'

# View page html code :
def viewPage( infile):
	'''
	Prints HTML code from infile
	'''

	page = urllib.urlopen(infile).read()
	try:
		print page

	except ValueError:
        	return 'Unable to View Page'

# Archive page html File :
def archivePage(pagename, infile):
	'''
	Archives HTML infile with appended time stamp
	'''

	f = urllib.urlopen(infile).read()
	date = time.strftime('.v%Y%m%d_%H%M%S')
	outfile = '/home/gfurlich/Website/archive/'+pagename+'_index.html'+date

	# Compare with last archived file :  

	try:
		subprocess.call(['cp',infile,outfile])
		return '\tCopied'+infile+' -> '+outfile 

	except ValueError:
        	return 'Unable to copy HTML File'

# Read html tag from page into array :
def readTag( infile, tag ):
	'''
	Reads in HTML code from infile, searchs for tag and reads tag contents into list by line
	'''
	
	page = urllib.urlopen(infile).read()
	itag = '<'+tag+'>'
	ftag = '</'+tag+'>'

	try:
		start = page.index(itag) + len(itag)
		end = page.index(ftag, start )
		inbetween = page[page.find(itag)+len(itag):page.find(ftag)]
		inbetween = re.split("\n",inbetween)
		return inbetween

	except ValueError:
        	return 'Unable to read Tag'

# Find and veiw html code between html tag :
def viewTag( infile, tag ):
	'''
	Reads in HTML code from infile, searchs for tag and prints tag contents
	'''

	page = urllib.urlopen(infile).read()
	itag = '<'+tag+'>'
	ftag = '</'+tag+'>'

	try:
		start = page.index(itag) + len(itag)
		end = page.index(ftag, start )
		inbetween = page[page.find(itag)+len(itag):page.find(ftag)]
		print inbetween

	except ValueError:
        	return 'Unable to view Tag'

# Remove tag content from html code :
def removeTag(pagename,infile,tag):
	'''
	Reads in HTML code from infile, searchs for tag and removes tag contents
	'''

	page = readPage(infile)
	tag_contents = readTag(infile,tag)
	
	try:

		# Removing Tag contents
		print 'Removing Contents from Tag <'+tag+'>...</'+tag+'>'

		for i in range(len(tag_contents) - 2):
        		j = page.index('<'+tag+'>') + 1
			print page[j]
			del page[j]
		
		# archive old file, delete, and then write new one :
		archivePage(pagename,infile)
		subprocess.call(["rm",infile])

		# Write to file
		f = open(infile, "w+")
		for lines in range(len(page)):
        		f.write(page[lines]+"\n")

	except ValueError:
        	return 'Unable to remove Tag'
		

# Replace html code between html tag :
def replaceTag(pagename,infile, tag, replacement_contents):
	'''
	Reads in HTML code from infile, searchs for tag and replaces tag contents. replacement_contents must be a list of each line in different. 
	'''

	page = readPage(infile)
	tag_contents = readTag(infile,tag)
	replacement_contents = re.split("\n",replacement_contents)

	# Skip Replacment if Contents Match :
	#print tag_contents[1:-1], replacement_contents
	if tag_contents[1:-1] == replacement_contents :
#	if tag_contents == replacement_contents :
		print 'Skipping Tag <'+tag+'>...</'+tag+'> , Current Contents Match Replacement \n'

	else :
		try:

			# Removing Tag contents :
			print 'Removing Contents from Tag <'+tag+'>...</'+tag+'>'

			for i in range(len(tag_contents) - 2):
				j = page.index('<'+tag+'>') + 1
				print page[j]
				del page[j]

			# Add new Tag contents :
			print 'Adding Contents to Tag <'+tag+'>...</'+tag+'>'
	
			for i in range(len(replacement_contents)):
				print replacement_contents[i]
				page.insert(page.index('<'+tag+'>') + 1 + i, replacement_contents[i])

			# archive old file, delete, and then write new one :
			archivePage(pagename,infile)
			subprocess.call(["rm",infile])

			# Write to file :
			f = open(infile, "w+")
			for lines in range(len(page)):
				f.write(page[lines]+"\n")

		except ValueError:
			return "Unable to replace Tag"

#--- End of Script ---#
