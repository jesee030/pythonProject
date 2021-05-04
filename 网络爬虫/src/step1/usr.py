#!/usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup

def Evidence(date):
    #	date为给定日期
    #   请在此添加实现代码   #
    # ********** Begin *********#
    response = requests.get("https://www.guet.edu.cn/jy/zhaopin.jsp?a165823t=475&a165823p=20&a165823c=100&urltype=tree.TreeTempUrl&wbtreeid=1003")

    url = "https://www.guet.edu.cn/jy/zhaopin.jsp?a165823t=475&a165823p=1&a165823c=10&urltype=tree.TreeTempUrl&wbtreeid=1003"
    soup = BeautifulSoup(response.text, 'html.parser')
    # soup = BeautifulSoup(url, 'lxml')
    # print(soup.prettify())
    # print(response.text)
    # results = soup.find("div",class_="jiuye zhaopin")
    # print(results.select("span"))

    #get every employ title
    # titles = soup.find_all("li")
    # for title in titles:
    #     post = title.find("span")
    #     if post:
    #         print(post.getText())
    # date = input()
    titles = soup.find_all("li",class_=None)
    for title in titles:
        post = title.find("a")
        # print(post)
        if post:
            # print(post)
            a = post.getText().replace('\n','').replace('\r','').replace('\t','')
            # print(a)
            #b is date
            b=a[-10:]
            # print(b)
            if b==date:
                #print the info
                print(a[:-10])
        # a=post.text.strip()
    #     for i in a:
    #         if i.isdigit() or i== "-":
    #             print(i,end="")
    # print()

        # print(post.getText())
    # a = title.find("a")
    # if a:
    #     print(a.getText())
    # for ti in title:
    #     t = ti.find("span")
    #     if t:
    #         print(t.getText())
# for result in results:
#     print(result.se)
    # ********** End **********#