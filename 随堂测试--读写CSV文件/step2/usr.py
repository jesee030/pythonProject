import csv
def readcsv():
 #        请在此处添加代码         #
 # *************begin************#
	 with open("book.csv", "r", newline="", encoding='utf-8') as csvfile:
		 csvreader = csv.reader(csvfile)
		 for row in csvreader:
			 #跳过文件头
			 if csvreader.line_num == 1:
				 continue
			 print(row)
 # **************end*************#



if __name__ == '__main__':
	readcsv()