#!/usr/bin/env python
#-*- coding: utf-8 -*-


from utils.utils import BasicHandler


class HomeHandler(BasicHandler):
    def get(self):
        self.render("index.html")


class EnglishProfileHandler(BasicHandler):
    def get(self):
        self.render("profile_en.html")


class ChineseProfileHandler(BasicHandler):
    def get(self):
        self.render("profile_ch.html")
