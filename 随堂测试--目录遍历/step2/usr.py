#使用深度优先遍历目录
import os
import os.path
def listDirWidthFirst(path):
    """
    广度遍历优先算法遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
# *************begin************#
    try:
        a=[]
        a.append(path)
        x=a.pop()
        for i in os.listdir(x):
            a.append(x+os.sep+i)
        a.sort()
        while a != []:
            x=a.pop(0)
            if os.path.isdir(x):
                for i in os.listdir(x):
                    a.append(x+os.sep+i)
            print(x)
    except FileNotFoundError:
        print(path+" is not a directory or does not exist.")

# **************end*************#  


#遍历当前目录下的test目录
path = input()
listDirWidthFirst(path)