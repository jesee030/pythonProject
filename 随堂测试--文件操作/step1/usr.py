# 统计大写字母出现的次数，并按照字母出现次数降序排序输出
def countchar(file):
    # *************begin************#
    adict = {}  # 记录字母对应出现次数的空字典
    fb = open(file, 'r')
    ch = fb.read()  # 以单个字符返回
    # print(ch)
    for i in ch:
        if i.isupper():
            if i in adict:
                adict[i] += 1
            else:
                adict[i] = 1
    # reverse=True->降序
    s=sorted(adict.items(), key=lambda e: e[1], reverse=True)
    for i in s:
        print(i)


# **************end*************#


file = input()
countchar(file)
