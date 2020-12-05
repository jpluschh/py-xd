#! /usr/bin/python3

import bs4
import requests
import string
import re
import argparse
import sys

url = ''

r = requests.get(url)
html_doc = r.text

soup = bs4.BeautifulSoup(html_doc, 'html.parser')

airdates = soup.find_all("div", {"class": "airdate"})

titles = soup.find_all("a", itemprop = "name")


filename = "titles.txt"

f = open(filename, "a")
f.write(str(airdates))
f.write(str(titles))
f.close()
