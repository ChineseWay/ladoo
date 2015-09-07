__author__ = 'zhuangzebo'

# from mail import mailGun
from mail import mailUser

def uploadUser(body):
    lines = body.split("\n")
    if len(lines) == 1:
        lines = body.split("\r")

    users = []
    for line in lines:
        for u in line.split(','):
            if not u:
                continue
            users.append(str(u))
    users = [str(u) for u in lines]
    mailUser.add(users)


def getUsers():
    users = mailUser.get()
    return users


def sendMail(sender, receiver, subject, text):
    receiver = receiver.split(";")
    if not receiver:
        return

    mailUser.sendMail(sender, receiver, subject, text)
    return




