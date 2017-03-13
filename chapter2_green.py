#!/usr/bin/python

import urllib
from bs4 import BeautifulSoup

# 目标URL
# the real one
#url = 'http://www.pythonscraping.com/pages/warandpeace.html'

# the same file on my local machie
url = 'file:///home/zeroway/github/wswp/warandpease.html'

# 获取对URL的请求
req = urllib.request.Request(url)

# 添加浏览器代理设置(可选项)
req.add_header("User-agent", "Mozilla 5.10")

# 打开URL
conn = urllib.request.urlopen(req)

# 获取网页内容
context = conn.read()

soup = BeautifulSoup(context, "html5lib");

# 匹配所有<span class="green"></span> 的tags
# findAll(tagName, tagAttributes)
nameList = soup.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
