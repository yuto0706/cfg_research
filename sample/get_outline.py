#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from HTMLParser import HTMLParser


def GetMoviePageHTMLFromId(movie_id):
	url_prefix = 'http://eiga.com/movie/'
	html = urllib2.urlopen(url_prefix + str(movie_id) + '/').read().decode('utf-8')
	return html

class MoviePageHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.isOutline = False
		self.isOutlineBody = False
		self.outline = ''

	def handle_starttag(self, tag, attrs):
		attrs = dict(attrs)
		if tag == 'div':
			if 'class' in attrs and attrs['class'] == 'outline':
				self.isOutline = True
		elif tag == 'p' and self.isOutline:
				self.isOutlineBody = True

	def handle_data(self, data):
		if self.isOutlineBody:
			self.outline = data
			self.isOutline = False
			self.isOutlineBody = False

def GetMovieOutlineFromHTML(movie_page_html):
	parser = MoviePageHTMLParser()
	parser.feed(movie_page_html)
	parser.close()
	return parser.outline

def test():
	movie_id_start = 1150
	movie_id_end = 1160
	for movie_id in range(movie_id_start, movie_id_end):
		movie_page_html = GetMoviePageHTMLFromId(movie_id)
		movie_outline = GetMovieOutlineFromHTML(movie_page_html)
		print movie_outline
	return

test()
