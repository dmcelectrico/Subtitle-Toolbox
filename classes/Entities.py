#!/usr/bin/python
# -*- coding: utf-8 -*-

class Subtitle:
	""" Holds the url and language of a single subtitle. """

	def __init__(self, language,url,encoding='UTF-8'):
		self.language=language
		self.url=url
		self.encoding=encoding

	def __str__(self):
		return "Language: "+self.language+"\tURL: "+self.url+"\n"

	def encoding():
		doc = "The encoding property."
		def fget(self):
			return self._encoding
		def fset(self, value):
			self._encoding = value
		def fdel(self):
			del self._language
		return locals()
	encoding = property(**encoding())

	def language():
		doc = "The language property."
		def fget(self):
			return self._language
		def fset(self, value):
			self._language = value
		def fdel(self):
			del self._language
		return locals()
	language = property(**language())

	def url():
		doc = "The url property."
		def fget(self):
			return self._url
		def fset(self, value):
			self._url = value
		def fdel(self):
			del self._url
		return locals()
	url = property(**url())

	__repr__=__str__

class SubtitleRelease:
	""" Holds the subtitles (Subtitle) for an episode's release. """

	def __init__(self, release):
		self._subtitles = []
		self.release=release

	def __str__(self):
		string = "Release: " + self.release + "\n"
		for subtitle in self.subtitles:
			string+="\t"
			string += str(subtitle)
		return string

	def release():
		doc = "The release property."
		def fget(self):
			return self._release
		def fset(self, value):
			self._release = value
		def fdel(self):
			del self._release
		return locals()
	release = property(**release())

	def subtitles():
		doc = "The subtitles property."
		def fget(self):
			return self._subtitles
		def fset(self, value):
			self._subtitles = value
		def fdel(self):
			del self._subtitles
		return locals()
	subtitles = property(**subtitles())

	def add(self,subtitle):
		self.subtitles.append(subtitle)

	__repr__=__str__

class Episode:
	""" Holds the subtitles (SubtitleRelease) from the several releases of an episode. """

	def __init__(self,series=None,season=None,episode=None,title=None,path=None,filename=None):
		self.series=series
		self.season=season
		self.episode=episode
		self.title=title
		self.path=path
		self.filename=filename

	def __str__(self):
		string = self.series+" S"+str(self.season).zfill(2)+"E"+str(self.episode).zfill(2)+" - "+self.title
		return string

	def series():
		doc = "The series property."
		def fget(self):
			return self._series
		def fset(self, value):
			self._series = value
		def fdel(self):
			del self._series
		return locals()
	series = property(**series())

	def season():
		doc = "The season property."
		def fget(self):
			return self._season
		def fset(self, value):
			self._season = value
		def fdel(self):
			del self.season
		return locals()
	season = property(**season())


	def episode():
		doc = "The episode property."
		def fget(self):
			return self._episode
		def fset(self, value):
			self._episode = value
		def fdel(self):
			del self._episode
		return locals()
	episode = property(**episode())

	def title():
		doc = "The episode title."
		def fget(self):
			return self.title
		def fset(self, value):
			self.title = value
		def fdel(self):
			del self.title
		return locals()
	title = property(**title())

	def releases():
		doc = "The releases property."
		def fget(self):
			return self._releases
		def fset(self, value):
			self._releases = value
		def fdel(self):
			del self._releases
		return locals()
	releases = property(**releases())