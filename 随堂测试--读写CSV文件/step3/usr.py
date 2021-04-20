import csv


def readcsv():
    #        请在此处添加代码         #
    # *************begin************#
    with open("book.csv", "r", newline="", encoding='utf-8') as csvfile:
        # 3.8:使用DictReader，和reader函数类似，接收一个可迭代的对象，能返回一个生成器，但是返回的每一个单元格都放在一个字典的值内，而这个字典的键则是这个单元格的标题（即列头）。
        csvreader = csv.DictReader(csvfile)
        # columns = [row for row in csvreader]
        # print(columns)




            
            
        #3.6
        # csvreader = csv.reader(csvfile)
        # out=[]
        # low1=[]
        # low2=[]
        #
        # for row in csvreader:
        #     low1.append(row[0])
        #     low2.append(row[1])
        # for row in low1:
        #     out.append("{"+low1[1])
        #
        # print(out)
        # print(low1)
        # print(low2)
      

# **************end*************#


if __name__ == '__main__':
    readcsv()
