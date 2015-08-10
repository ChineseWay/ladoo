#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import logging
import argparse

from tornado.ioloop import IOLoop
from tornado.web import Application, url
from settings import settings

class App(object):

    def __init__(self):
        self.root_path = self.init_path()  
        self.handlers = self.init_handler()

    def init_path(self):
        f = os.path.abspath(__file__)
        path = os.path.dirname(f)
        sys.path.append(path)
        return path

    def init_handler(self):
        assert os.path.exists(self.root_path), "'%s' does not exist." % self.root_path

        files = os.listdir(self.root_path)

        handlers = []
        for f in files:
            p = os.path.join(self.root_path, f) 
            if not os.path.isdir(p):
                continue
            u = os.path.join(p, "urls.py")
            if not os.path.exists(u):
                continue

            try:
                exec('from %s.urls import urls' % f)
                handlers.extend([url(*arg) for arg in urls])
            except Exception, e:
                logging.error("init handler err: %s", e)
        return handlers

    def listen(self, port=8888):
        app = Application(self.handlers, **settings)
        app.listen(port)


def main(port):
    app = App()
    app.listen(port)
    logging.warning("server starts to listen %d", port)

    IOLoop.current().start() 


if __name__ == '__main__':
    # parse port
    parser = argparse.ArgumentParser()  
    parser.add_argument("port", help="listen to the server port.", type=int)
    args = parser.parse_args()

    # execute application
    main(args.port)
