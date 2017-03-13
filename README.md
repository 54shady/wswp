# wswp
Web Scraping with Python

[书主页](http://www.pythonscraping.com/)

[原作者代码路径](https://github.com/REMitchell/python-scraping)

## 使用前的准备安装Beautiful Soup

[参考http://cuiqingcai.com/1319.html](http://cuiqingcai.com/1319.html)

Beautiful Soup 安装,需要root权限

	sudo emerge -v dev-python/pip

	sudo pip install beautifulsoup4

## Skeleton(Python 3.4.3)

导入必要模块

	import urllib
	from bs4 import BeautifulSoup

目标URL

	url = 'http://www.pythonscraping.com/exercises/exercise1.html'

获取对URL的请求

	req = urllib.request.Request(url)

添加浏览器代理设置

	req.add_header("User-agent", "Mozilla 5.10")

打开URL

	conn = urllib.request.urlopen(req)

获取网页内容

	context = conn.read()
	soup = BeautifulSoup(context, "html5lib");

exercises1.html内容见代码
