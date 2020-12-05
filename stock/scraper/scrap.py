#! usr/bin/env python3

from urllib.request import urlopen

url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

title_index = html.find("<title>")

start_index = title_index + len("<title>")

end_index = html.find("</title>")

title = html[start_index:end_index]

print(title)
