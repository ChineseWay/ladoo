#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import redis

from pymongo import MongoClient
from tornado.web import RequestHandler
from settings import MONGO_HOST, MONGO_PORT
from settings import REDIS_HOST, REDIS_PORT

class BasicHandler(RequestHandler):
    '''basic handler'''

    def get(self):
        pass

    def post(self):
        pass

    def head(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass



class MongoConn(object):
    _conn = {}

    @staticmethod
    def getConn():
        pid = os.getpid()
        if pid not in MongoConn._conn:
            MongoConn._conn[pid] = MongoClient(MONGO_HOST, MONGO_PORT)
        return MongoConn._conn[pid]


class RedisConn(object):
    _conn = {}

    @staticmethod
    def getConn():
        pid = os.getpid()
        if pid not in RedisConn._conn:
            RedisConn._conn[pid] = redis.Connection(REDIS_HOST, REDIS_PORT)
        return RedisConn._conn[pid]


