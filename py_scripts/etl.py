#! /usr/bin/python3

import bs4
import requests
import string
import re
import argparse
import sys

#set date
d = sys.argv[1]

# telegraph url
url = sys.argv[2]

r = requests.get(url)
html_doc = r.text

soup = bs4.BeautifulSoup(html_doc, 'html.parser')

figure_tags = soup.find_all('figure')

separate_links = str(figure_tags).replace('\"', '\n')

re_sl = re.sub("\/file\/", "https://telegra.ph/file/", separate_links)

links_list = re.findall("https?://\S+.jpg", re_sl)

filename = "%s-links.txt" % d

f = open(filename, "a")
f.write('\n'.join(links_list[l] for l in range(len(links_list))))
f.close()
