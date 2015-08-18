#!/usr/bin/env python
#-*- coding: utf-8 -*-


from utils.utils import BasicHandler


class HomeHandler(BasicHandler):
    def get(self):
        self.render("index.html")


class EnglishProfileHandler(BasicHandler):
    def get(self):
        self.render("profile_en.html")


class ChineseProfileHandler(BasicHandler):
    def get(self):
        self.render("profile_ch.html")
#        self.render("test.html")


class SendCloudHandler(BasicHandler):
	def get(self):
		self.render("sendmail.html")

	def post(self):
		print self.request.arguments
		self.write("OK")