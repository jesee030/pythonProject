"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化方法

        :param name: 姓名
        """
        #        请在此处添加代码       #
        # *************begin************#
        # print('call Employee __init__')

        self.__name = name

        # **************end*************#

    @property
    def name(self):
        '''返回姓名'''
        #        请在此处添加代码       #
        # *************begin************#
        # print('call Employee name')

        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        # **************end*************#

    @abstractmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass




class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        """
              初始化方法

              :param name: 姓名
              :param working_hour：工作时长

              """
        #        请在此处添加代码       #
        # *************begin************#
        super().__init__(name)
        self.__working_hour=working_hour
        # print('call Programmer __init__')

        # **************end*************#

    @property
    def working_hour(self):
        '''返回工作时长'''
        #        请在此处添加代码       #
        # *************begin************#
        # print('call Programmer 返回工作时长')

        return self.__working_hour
        # **************end*************#

    @working_hour.setter
    def working_hour(self, working_hour):
        '''
        设置工作时长
        :param working_hour:工作时长
        '''
        #        请在此处添加代码       #
        # *************begin************#
        # print('call Programmer 设置工作时长')

        self.__working_hour=working_hour

        # **************end*************#

    def get_salary(self):
        '''返回程序员所得工资'''
        #        请在此处添加代码       #
        # *************begin************#
        # print('call Programmer 返回程序员所得工资')
        return self.__working_hour * 150.0

        # **************end*************#



class Salesman(Employee):
    """销售员"""


    def __init__(self, name, sales=0):
        """
                   初始化方法

                   :param name: 姓名
                   :param sales：销售额

                   """
        #        请在此处添加代码       #
        # *************begin************#
        super().__init__(name)
        self.__sales=sales
        # print('call Salesman __init__')


        # **************end*************#

    @property
    def sales(self):
        '''返回销售额'''
        #        请在此处添加代码       #
        # *************begin************#
        # print('call Salesman sales')

        return self.__sales

        # **************end*************#

    @sales.setter
    def sales(self, sales):
        '''
        设置销售额
        :param sales:销售额
        '''
        #        请在此处添加代码       #
        # *************begin************#
        self.__sales=sales
        # print('call Salesman 设置销售额')

        # **************end*************#

    def get_salary(self):
        '''返回销售员所得工资'''
        #        请在此处添加代码       #
        # *************begin************#
        # print('call Salesman 返回销售员所得工资')

        return self.__sales * 0.05 + 1200
        # **************end*************#



