def is_palindrome(num):
    """
    判断一个数是不是回文数
    :param num: 正整数
    :return: 是回文数返回True，不是回文数返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    if num == int(str(num)[::-1]):
        return True
    return False
    # **************end*************#
