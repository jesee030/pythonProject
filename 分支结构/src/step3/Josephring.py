'''《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，
报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
'''

def main():
    #        请在此处添加代码       #
    # *************begin************#
    positions = [True]*30
    dead, index, number = 0, 0, 0
    while dead < 15:
        if positions[index]:
            number+=1
            if number==9:
                positions[index]=False
                dead+=1
                number=0
        index+=1
        #make sure won't index out off range
        index%=30

    for position in positions:
        print('1' if position else  '0',end='')



    # **************end*************#


if __name__ == '__main__':
    main()