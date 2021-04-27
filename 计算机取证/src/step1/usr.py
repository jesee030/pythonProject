import zipfile
import itertools

def Try():
    path = 'D:\pythonProject\计算机取证\src\step1\evil.zip' #压缩文件路径
    Try.password=None
    #破解并返回密码
    #   请在此添加实现代码   #
    # ********** Begin *********#
    zfile = zipfile.ZipFile(path)
    #排列：itertools.permutations(iterable[, r])
    # 将其中的元素排列为所有可能的情况，并以元组序列的形式返回
    for i in itertools.permutations('012345asd',6):
        mylist=(''.join(i))
        # print(mylist)
        try:
            Try.password = mylist
            # print(Try.password)
            zfile.extractall(pwd=str(mylist).encode("utf-8"))
            break
        except Exception as e:
            # print("error")
            pass
            # finally:
            #     zipFile.close()  # 关闭文件
    return Try.password
    # ********** End **********#

