def is_prime(num):
    """
    判断一个数是不是素数
    :param num: 正整数
    :return: 是素数返回True，不是素数返回False
    """
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False