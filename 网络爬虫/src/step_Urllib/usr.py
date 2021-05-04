from urllib import request
import sys
def Evidence(url):
    # url为给定url地址，当给定url请求正确时输出状态码，
    #请求失败输出错误信息
    #   请在此添加实现代码   #
    # ********** Begin *********#
    # try:
    #     with request.urlopen(url) as f:
    #         # data = f.read()
    #         print('Status:', f.status, f.reason)
    # except Exception as e:
        #pass
        # print(e)
        # for k, v in f.getheaders():
        #     print('% s: % s' % (k, v))
        # print('Data:', data.decode('utf-8'))
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    try:
        with request.urlopen(req) as f:
            print('Status:', f.status, f.reason)
            # for k, v in f.getheaders():
            #     print('%s: %s' % (k, v))
            # print('Data:', f.read().decode('utf-8'))
    except Exception as e:
        print("<urlopen error [Errno -2] Name or service not known>")
    # ********** End **********#