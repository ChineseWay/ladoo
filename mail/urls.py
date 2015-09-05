__author__ = 'zhuangzebo'

from mail.views import SendMailHandler


urls = [
    (r"/send_mail/?", SendMailHandler),
]