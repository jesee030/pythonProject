"""
英制单位英寸和公制单位厘米互换
"""
def cmin(value,unit):
    ''':param value:长度，
        :param unit:单位'''

    #        请在此处添加代码       #
    # *************begin************#
    if (unit=="in" or unit=="英寸"):
        value = value * 2.54
        print("%.2f厘米"%value)
        return
    elif(unit=="cm" or unit=="厘米"):
        value /= 2.54
        print("%.2f英寸"%value)
        return
    else:print("请输入有效的单位")
    # **************end*************#
  

value = input()
value = int(value)
unit = input()
cmin(value,unit)