# coding: utf-8
__author__ = 'zhuangzebo'

from utils.utils import BasicHandler


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

 		sender = sender[0]
 		reciever = reciever[0]
 		subject = subject[0]
 		content = content[0]

		resp = Mail().send(reciever, sender, subject, content)

		msg += "<p>%s</p>" % str(resp)
		msg += "<p><a href='/send_mail'>返回</a></p>"
		self.write(msg)