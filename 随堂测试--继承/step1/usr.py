class BankEmployee():
 #        请在此处添加代码         #
 # *************begin************#
 # TODE
 # 本关任务：编写银行员工类BankEmployee，要求：
 # 1.银行员工类的属性包括姓名name，工号num，工资salary
 # 2.姓名name和工号num设置为私有属性,并将salay设置为默认参数3000
 #
    def __init__(self,name,num):
        self.__name=name
        self.__num = num
        self.salary=3000

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.__name]
     
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.__name] = value
     
    def __delete__(self, instance):
        del instance.__dict__[self.__name]


    def get_salary(self):
        print("{}领到这个月工资{:d}".format(self.__name ,self.salary))


 # **************end*************#

def main():
    name = input()
    num = input()
    bankemployee = BankEmployee(name,num)
    bankemployee.get_salary()

if __name__=="__main__":
    main()