# coding: utf-8


import requests


class Mail(object):
	URL = "http://sendcloud.sohu.com/webapi/mail.send.json"
	API_USER = 'ladoo_freight'
	API_KEY = 'OJ1zd6ev1AaQjLML'

	def __init__(self):
		pass

	def send(self, to, _from, subject, content):
		params = {                                                                      
	    	"api_user": self.API_USER, 	# 使用api_user和api_key进行验证                       
		    "api_key" : self.API_KEY,                                             
		    "to" : to, 					# 收件人地址, 用正确邮件地址替代, 多个地
		    "from" : _from, 			# 发信人, 用正确邮件地址替代     
		    "fromname" : "Ladoo Freight",                                                    
		    "subject" : subject,                              
		    "html": content,  
		    "resp_email_id": "true",
		}

		r = requests.post(self.URL, data=params)
		return r.text  