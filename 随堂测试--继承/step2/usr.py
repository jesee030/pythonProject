class BankEmployee():
    def __init__(self,name="",num="",salary=3000): 
        self.__name = name
        self.__num = num
        self.salary = salary
    def get_salary(self): #定义领工资方法get_salary()
        print("%s领到这个月工资%d"%(self.__name,self.salary))
    # 请在此处添加代码对name和num设置set/get方法 #
 	# *************   begin   ************#
    # 任务描述
    # 本关任务：编写一个银行柜员类BankTeller，继承BankEmployee类，要求：
    # 1.
    # 完善BankEmployee类，对私有属性name和num添加set方法和get方法以实现对私有属性的设置和获取
    # 2.
    # 对工号的合法性进行检验，要求工号以字母s开头，如s678是合法工号，678
    # 不是合法工号
    # 3.
    # 继承BankEmployee类，定义银行柜员类BankTeller类，其name属性和num属性和父类BankEmployee类相同，属性salary默认参数为2000
    def get_name(self):
        return self.__name
    def get_num(self):
        if str(self.__num).startswith('s'):
            return self.__num
        else:
            print("工号以s开头")
    def set_name(self, name):
        self.__name=name
    def set_num(self, num):
        if str(num).startswith('s'):
            self.__num = num
        else:
            self.__num = None
            print("工号以s开头")

 	# **************  end   *************#

  
class BankTeller(BankEmployee):
 #        请在此处添加代码         #
 # *************begin************#
    def set_name(self,name):
        BankEmployee.set_name(self,name)
    def set_num(self,num):
        #print(num)
        BankEmployee.set_num(self,num)


    def get_salary(self):
        self.salary=2000
        BankEmployee.get_salary(self)
    def get_name(self):
         return BankEmployee.get_name(self)
    def get_num(self):
        return BankEmployee.get_num(self)

 # **************end*************#
        
def main():
    bankteller = BankTeller()
    name = input()
    num = input()
    bankteller.set_name(name)
    bankteller.set_num(num)
    bankteller.get_salary()
    print(bankteller.get_name(),bankteller.get_num())
    
if __name__=="__main__":
    main()