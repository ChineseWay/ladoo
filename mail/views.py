# coding: utf-8
__author__ = 'zhuangzebo'

from utils.utils import BasicHandler
from models import uploadUser, getUsers, sendMail

class UserList(BasicHandler):

    def get(self):
	 	self.write("user...")


class UploadUserHandler(BasicHandler):

	def post(self):
		body =  self.request.files['upload'][0]['body']
		uploadUser(body)
		self.redirect("/send_mail")

	def get(self):
		users = getUsers()
		self.render("upload.html", users=users)



class SendMailHandler(BasicHandler):
	def get(self):
		users = getUsers()
		self.render("upload.html", users=users)

	def post(self):
		sender = self.request.arguments.get("sender")
		receiver = self.request.arguments.get("receiver")
		subject = self.request.arguments.get("subject")
		content = self.request.arguments.get("content")

		print self.request.arguments
		msg = ""
		if not sender:
			msg += "<p>没有发件人</p>"

		if not receiver:
			msg += "<p>没有收件人</p>"
		if not subject:
			msg += "<p>没有标题</p>"
		if not content:
			msg += "<p>内容为空</p>"

 		sender = sender[0]
 		receiver = receiver[0]
 		subject = subject[0]
 		content = content[0]


		sendMail(sender, receiver, subject, content)

		msg = "<p><a href='/send_mail'>返回</a></p>"
		self.write(msg)