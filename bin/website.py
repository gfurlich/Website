#!/usr/bin/env python
'''
File : website.py
Author : Greg Furlich
Date Created : 9/17/2017

Purpose : Use the toolbox of editwebsite.py to modify all pages of gregfurlich.com.

Execution : website.py

'''

# Python Libraries	
import editwebsite as ws

#--- Pages Tags ---#

# Pages HTML Code #
# Array containing pages information :

pages = [
# Page		Directory:		Page Subtitle
['Home',	'../',			'Welcome U of Utah'	],
['CV',		'../cv/',		'Ciriculum Vitea'	],
['Research',	'../research/',		'Research'		],
['Hobbies',	'../hobbies/',		'Hobbies'		],
['Projects',	'../projects/',		'Projects'		],
['Photography',	'../photography/',	'Photography'		]
]

n_pages = len(pages)


# Navigation Code #

nav = """        

	<!---<div class="hex">
		<div class="top"></div>
		<div class="bottom"></div>
	</div>--->

	<img class="img-circle" src="Antelope Island.jpg"  width="200 px" height="200 px">

	<a href="../"><p>Home</p></a>
	<a href="../cv/"><p>CV</p></a>
	<a href="../research/"><p>Research</p></a>
	<a href="../hobbies/"><p>Hobbies</p></a>
	<a href="../projects/"><p>Projects</p></a>
	<a href="../photography/"><p>Photography</p></a>

"""

# Footer Code #
footer = """
	&copy Greg Furlich 2017 <br>
	All Rights Reserved
"""

# Header Code #
header = """
	<h> Greg Furlich</h><br>
	<hl>======<br>
"""

# Modifying all Pages :

for i in range(0,n_pages) :

	page = '../src/'+pages[i][1][3:]+'index.html'
	pagename = pages[i][0]
	pageSubtitle = '\t<hl>'+pages[i][2]+'\n'

	print 'Modifying Page : '+page+'\n'

	ws.replaceTag(pagename,page,'nav',nav)
	ws.replaceTag(pagename,page,'footer',footer)
	ws.replaceTag(pagename,page,'header',header+pageSubtitle)


#--- End of Script ---#
