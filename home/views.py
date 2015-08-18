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
		sender = self.request.arguments.get("sender")
		reciever = self.request.arguments.get("reciever")
		subject = self.request.arguments.get("subject")
		content = self.request.arguments.get("content")

		print sender, reciever, subject, content 
		self.write("OK")