#!/usr/bin/env python
#-*- coding: utf-8 -*-


from utils.utils import BasicHandler


class HomeHandler(BasicHandler):
    def get(self):
        self.write("hello world")
