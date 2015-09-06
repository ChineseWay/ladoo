__author__ = 'zhuangzebo'

from views import SendMailHandler, UploadUserHandler


urls = [
    (r"/send_mail/?", SendMailHandler),
    (r"/upload/?", UploadUserHandler)
]