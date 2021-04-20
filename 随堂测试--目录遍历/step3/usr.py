import os
import os.path
def listDiroswalk(path):
    """
    使用os.walk遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
# *************begin************#
    try:
        for main,Dir,File in os.walk(path):
            for i in Dir:
                print(main+os.sep+i)
            for i in File:
                print(main+os.sep+i)
        os.chdir(path)
    except FileNotFoundError:
        print(path+" is not a directory or does not exist.")
        
# **************end*************#  


#遍历当前目录下的test目录
path = input()
listDiroswalk(path)