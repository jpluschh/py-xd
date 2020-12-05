#! /usr/bin/python3

import os

stockCode = '2330'
path = "/home/jpluschh/Downloads/" + stockCode

try:
    os.makedirs(path)
except OSError:
    print("Directory creation %s failed" % path)
else:
    print("Directory creation %s success" % path)

