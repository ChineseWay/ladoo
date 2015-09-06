#-*- coding: utf-8 -*-

import os

'''
    settings
'''

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "cookie_secret": "YzlhMGI2NTMxNTVhMjc4ZGFkMzE3MjJiZGY1ZGE2YjM4YzJjODU0Zg==",
    "xsrf_cookies": True,
}


MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

MAILGUN_API = "https://api.mailgun.net/v3/ladoo-freight.com/messages"
MAILGUN_KEY = "key-b3837395590b9ae45fbd3a534ea5ea06"