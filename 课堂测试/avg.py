data = [200, 388, 123, 456, 987, 342, 767, 234, 124, 345, 123, 234]


# 设计specifty函数的参数以及函数的功能,以实现计算任意月份的平均访客量
# *************begin************#
def specifty(*index):
    sun = 0
    for i in index:
        sun += data[i]
    avg = sun / len(index)
    print("%.2f"%avg)
    return avg


# **************end*************#


specifty(1, 2, 3, 4)  # 计算2-5月的平均访客量
specifty(10, 9, 8, 7, 6)  # 计算11-7月的平均访客量