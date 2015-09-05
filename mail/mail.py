# coding: utf-8
__author__ = 'zhuangzebo'


import requests


API = "https://api.mailgun.net/v3/ladoo-freight.com/messages"
KEY = "key-b3837395590b9ae45fbd3a534ea5ea06"


class MailGun(object):

    def __init__(self):
        self._request = requests.session()
        self._users = []

    def sendMail(self, from_, to=[], subject="", text=""):
        return self._request.post(
            API,
            auth=("api", KEY),
            data= {
                "from": from_,
                "to": to,
                "subject": subject,
                "text": text
            }
        )

    def addUser(self, users=[]):
        for u in users:
            if u in self._users:
                continue
            self._users.append(u)
        return

    def getUser(self):
        return self._users

    def getByPage(self, page=1, pageSize=50):
        total = len(self._users)
        return total, self._user[pageSize*(page-1): pageSize*page]



if __name__ == "__main__":
    mg = MailGun()
    from_ = "348284770@qq.com"
    to = ["zebozhuang@163.com"]
    subject = "hello world"
    text = "welcome to my world."
    res = mg.sendMail(from_, to, subject, text)
    print res.text