#!/usr/bin/ebv python
# -*- coding: utf-8 -*-

import requests
import sys
from queue import Queue
import threading
from bs4 import BeautifulSoup as bs
import re
import base64

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, compress',
	'Accept-Language': 'en-us;q=0.5,en;q=0.3',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
	}

class BaiduSpider(threading.Thread):
	"""docstring for ClassName"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			url = self._queue.get()
			try:
				self.spider(url)
			except Exception as e:
				print(e)
				pass

	def spider(self,url):
		#   请在此添加实现代码   #
		# ********** Begin *********#

		# ********** End **********#



def Evidence(keyword):
	queue = Queue()
	# md5加密关键字

	#   请在此添加实现代码   #
	# ********** Begin *********#

	# ********** End **********#

	# 爬取页数
	for i in range(1, 47):
		#   请在此添加实现代码   #
		# ********** Begin *********#

		# ********** End **********#

	# 多线程
		threads = []
		thread_code = 5
	#   请在此添加实现代码   #
	# ********** Begin *********#

	# ********** End **********#