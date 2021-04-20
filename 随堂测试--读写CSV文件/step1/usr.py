import csv


def readcsv():
    #        请在此处添加代码         #
    # *************begin************#
    with open("book.csv", "r", newline="", encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row[0])


# **************end*************#


if __name__ == '__main__':
    readcsv()
