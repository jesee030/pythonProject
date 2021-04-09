from isprime import is_prime
from ispalindrome import is_palindrome
def prime_palindrome(num):
    """
        判断一个数是不是回文素数
        :param num: 正整数
        :return: 是回文素数返回True，不是回文素数返回False
        """
    #        请在此处添加代码       #
    # *************begin************#
    if(is_palindrome(num) and is_prime(num)):
        return True
    return False
    # **************end*************#


