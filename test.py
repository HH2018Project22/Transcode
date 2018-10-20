# -*- coding: utf-8 -*-
"""
Created on "Date"

@author : Nicolas
"""

import pickle

with open("test.obj","rb") as test:
    object = pickle.load(test)
    print(object)
