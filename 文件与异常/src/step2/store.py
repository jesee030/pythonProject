from math import sqrt
#本关任务：编写一个将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）。

def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def store():
    #         请在此处添加代码       #
    # *************begin************#
    with open('a.txt', 'w', encoding='utf-8') as file:
        for i in range(1,99):
            if is_prime(i):
                file.write(str(i)+'\n')
    with open('b.txt', 'w', encoding='utf-8') as fileb:
        for i in range(100,999):
            if is_prime(i):
                fileb.write(str(i)+'\n')
    with open('c.txt', 'w', encoding='utf-8') as filec:
        for i in range(1000, 9999):
            if is_prime(i):
                filec.write(str(i)+'\n')



    # **************end*************#



