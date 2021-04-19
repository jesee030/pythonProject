from searchword import *
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    line = [[0] * m] * n
    for i in range(n):
        line[i] = input().split(" ")
    word = input()
    print(exist(line, word))