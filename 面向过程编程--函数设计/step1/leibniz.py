def estimate_pi_by_leibniz(n_terms = 1000):
    """
    通过莱布尼兹公式计算 pi 值，此方法不容易得到 15 位精度的 pi 值
    莱布尼兹公式：π = 4/1 − 4/3 + 4/5 − 4/7 + 4/9 − 4/11…
    :param n_terms:计算项数 n，默认值 1000
    :return:返回保留小数点后15位的 pi 值
    """
    sum=0.0
    for i in range(n_terms):
        sum+=(-1.0)**i/(2.0*i+1.0)
    sum*=4
    sum=round(sum,15)
    return sum