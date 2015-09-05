#!/usr/bin/env python
# -*- coding: utf-8 -*-

from home.views import HomeHandler
from home.views import EnglishProfileHandler
from home.views import ChineseProfileHandler


urls = [
    (r"/", HomeHandler),       
    (r"/profile/en/?", EnglishProfileHandler),
    (r"/profile/ch/?", ChineseProfileHandler),
]
