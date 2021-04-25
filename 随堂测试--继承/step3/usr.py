class BankEmployee():
 #    请在此处添加代码 设置插槽    #
 # *************begin************#
 # 任务描述
 # 本关任务：编写一个银行柜员类BankTeller，继承BankEmployee类，要求：
 # 1.
 # 完善BankEmployee类，对私有属性name和num添加set方法和get方法以实现对私有属性的设置和获取
 # 2.
 # 对工号的合法性进行检验，要求工号以字母s开头，如s678是合法工号，678
 # 不是合法工号
 # 3.
 # 继承BankEmployee类，定义银行柜员类BankTeller类，其name属性和num属性和父类BankEmployee类相同，属性salary默认参数为2000
    __slots__ = 'name','num','salary'
 # **************end*************#
    def __init__(self,name="",num="",salary=3000): 
        self.__name = name
        self.__num = num
        self.salary = salary
    def get_salary(self): #定义领工资方法get_salary()
        print("%s领到这个月工资%d"%(self.__name,self.salary))
    def set_name(self,name):
        self.__name = name
    
    def get_name(self):
        return self.__name
            
    def set_num(self,num):
        if num.startswith("s"):
            self.__num = num
        else:
            print("工号以s开头")
    def get_num(self):
        return self.__num

#commission 提成
class BankManager(BankEmployee):
# 请在此处添加代码 完成BankTeller类的定义#
# ************* begin  ************#
    def __init__(self,name,num,salary,commission):
        BankEmployee.set_name(self,name)
        BankEmployee.set_num(self,num)
        BankEmployee.salary=salary
        self.__commission = commission
    def get_commission(self):
        return self.__commission
    def get_commission(self):
        print("%s领到这个月提成%d"%(BankEmployee.get_name(self),self.__commission))


# ************** end  *************#
        
def main():
    name = input()
    num = input()
    salary = int(input())
    commission = int(input())
    bankmanager = BankManager(name,num,salary,commission)
    bankmanager.get_commission()
    
if __name__=="__main__":
    main()