import os
import os.path
def findfile(path,dstfile):
    """
    遍历目录中是否存在dstfile文件，如果存在输出该文件的内容，否则输出 dstfile does not exist.

    :param path: 需遍历的路径
    :dstfile: 需要查找的文件
    """
# *************begin************#
    try:
        x=0
        a,n=os.path.splitext(path)
        if n != "":
            raise NameError
        for main,Dir,File in os.walk(path):
            for i in File:
                if i == dstfile:
                    with open(main+os.sep+i,"r",encoding="utf-8") as f:
                            print(f.read())
                            x=1
        if x!=1:
            raise FileNotFoundError
    except FileNotFoundError:
        print(dstfile+" does not exist.")
    except NameError:
        print(path+" is not a directory or does not exist.")
# **************end*************#  


#遍历当前目录下的test目录
path = input()
file = input()
findfile(path,file)