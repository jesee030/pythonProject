# 统计一个文件中单词出现的次数，并输出出现次数最多的前3个单词
import itertools


def countword(file):
    with open(file, 'r') as fl:
        # create am empty direction
        wordfre = {}
        for line in fl:
            line = line.replace('.', '').replace(':', '').replace('"', '').replace(',', '')
            # print(line)
            # strip:去除换行符，Split:去除空格
            sword = line.strip().split()
            # print(sword)
            for word in sword:
                if word in wordfre:
                    wordfre[word] += 1
                    # print(word+str(wordfre[word]))
                else:
                    wordfre[word] = 1
                    # print(word+str(wordfre[word]))
        # print("wordfre",end='')
        # print(wordfre)
        # 键值对互换：

        # 未知错误，造成字典断裂

    # wordfre_new={v:k for k, v in wordfre.items()}

    # wordfre_new={}
    # for key,val in wordfre.items():
    #     wordfre_new[val]=key

    # wordfre_new = dict(zip(wordfre.values(),wordfre.keys()))
    # print("wordfre_new", end='')
    # print(wordfre_new)

    # wordfre = dict((value, key) for key, value in wordfre.items())

    # dict(wordfre.itervalues(),wordfre.iterkeys())
    # print("wordfre", end='')
    # print(wordfre)
    # print(sorted(wordfre.items(), key=lambda e: e[0], reverse=True))
    s = sorted(wordfre.items(), key=lambda e: e[1], reverse=True)

    # print("s", end='')
    # print(s)
    for i in s[:3]:
        x=i[1],i[0]
        print(x)


file = input()
countword(file)
