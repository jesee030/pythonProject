from decimal import Decimal
# Decimal思为十进制，这个模块提供了十进制浮点运算支持。
# 可以传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确。
import math
def estimate_pi_by_bbp(n_terms = 1000) -> float:
    """
    利用 Bailey–Borwein–Plouffe 公式进行计算，此方法可以得到 15 位精度的 pi 值
    :param n_terms:计算项数 n，默认值 1000
    :return:返回保留小数点后15位的 pi 值
    """
    pi= Decimal(0)
    for k in range(n_terms):
        pi+=(Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
    pi=round(pi,15)
    return pi