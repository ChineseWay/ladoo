#!/usr/bin/env python
#-*- coding: utf-8 -*-


from utils.utils import BasicHandler
from home.models import Mail

class HomeHandler(BasicHandler):
    def get(self):
        self.render("index.html")


class EnglishProfileHandler(BasicHandler):
    def get(self):
        self.render("profile_en.html")


class ChineseProfileHandler(BasicHandler):
    def get(self):
        self.render("profile_ch.html")
#        self.render("test.html")