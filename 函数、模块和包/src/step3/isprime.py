def is_prime(num):
    """
    判断一个数是不是素数
    :param num: 正整数
    :return: 是素数返回True，不是素数返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    for n in range(2,num):
        if(num % n == 0):
            return False
    return True
    # **************end*************#
