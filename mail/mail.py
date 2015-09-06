# coding: utf-8
__author__ = 'zhuangzebo'


import requests
import datetime

from settings import MAILGUN_API, MAILGUN_KEY
from utils.utils import MongoConn, RedisConn



class MailGun(object):

    def __init__(self):
        self._request = requests.session()
        self._users = []

    def sendMail(self, from_, to=[], subject="", text=""):
        return self._request.post(
            MAILGUN_API,
            auth=("api", MAILGUN_KEY),
            data= {
                "from": from_,
                "to": to,
                "subject": subject,
                "text": text
            }
        )


class MailUser(object):

    USER_ID_KEY = "user:id"

    def __init__(self):
        self.mailGun = MailGun()
        # self.mongoConn = MongoConn.getConn()
        # self.rdsConn = RedisConn.getConn()
        self._users = set()
        self._users_send = []

    # def genId(self):
    #     return self.rdsConn.incr(MailUser.USER_ID_KEY)

    def add(self, users=[]):
        self._users = self._users.union(users)

    def get(self):
        return list(self._users)

    def sendMail(self, from_, to, subject, text):
        for u in to:
            try:
                res = self.mailGun.sendMail(from_, u, subject, text)
                print res.json()
            except Exception, e:
                print e
            try:
                self._users.remove(u)
            except:
                pass
        self._users = set()

mailUser = MailUser()

if __name__ == "__main__":
    mg = MailGun()
    from_ = "348284770@qq.com"
    to = ["zebozhuang@163.com"]
    subject = "hello world"
    text = "welcome to my world."
    res = mg.sendMail(from_, to, subject, text)
    print res.text