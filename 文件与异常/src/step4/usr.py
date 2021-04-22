import json
#本关任务：编写一个能读写json文件的程序。
def main(name):
 #        请在此处添加代码         #
 # *************begin************#
    try:
        #写入json文件
        with open('data.json','w',encoding='utf-8') as fs:
            mylist=[]
            #读取txt文件
            dict={}
            with open(name,'r',encoding='utf-8')as file:
                #json.dump(dict,file)
                #fs.write(dict)
                #print(dict)
                #data operation
                flag = True
                name = ''
                price = ''
                for line in file:
                    # strip:去除换行符，Split:去除空格
                    word = line.strip().split()
                    print(word)
                    if flag:
                        name,price = word[0],word[1]
                        flag=False
                        continue
                    if not flag:
                        dict={}
                        dict[name],dict[price]=word[0],word[1]
                        #print(mydict)
                    #fs.write(json.dumps( mydict))
                    #print(mydict)
                        mylist.append(dict)
                    #fs.write(str(mylist))
                print(mylist)





    except IOError as e:
        print(e)


    # try:
    #     dic={}
    #     with open('data.json','r',encoding='utf-8') as fs:
    #        dic[0]=json.load(fs)
    #        print(dic)
    #
    # except IOError as e:
    #     print(e)

 # **************end*************#
        
if __name__ == '__main__':
    name = input()
    main(name)