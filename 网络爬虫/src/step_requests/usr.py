import requests

def Evidence(url):
	# url为给定url地址，当给定url请求正确时输出状态码，请求失败输出错误信息
	#   请在此添加实现代码   #
	# ********** Begin *********#
    try:
        with requests.get(url) as f:
            print("Status: %s"%f.status_code)
    except Exception as e:
        print("url请求失败")
	# ********** End **********#