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

		msg = ""
		if not sender:
			msg += "<p>没有发件人</p>"

		if not reciever:
			msg += "<p>没有收件人</p>"
		if not subject:
			msg += "<p>没有标题</p>"
		if not content:
			msg += "<p>内容为空</p>"

 		print sender, reciever, subjec没有发件人t, co
		
		ret = "<p><a href='/send_mail'>返回</a></p>"
		msg += ret 
		self.write(msg)