def exist(board, word):
    """
    完成了搜索功能
    :param board: 二维的字母表:list[list[str]]
    :param word: 待搜索的单词: str
    :return: 返回是否搜索到，如果有，则返回 true，否则返回 false
    """
    #为空返回
    if not board:
        return False
    m = len(board)
    #字符行为0返回
    if m == 0:
        return False
    #设置列->n
    n = len(board[0])
    #初始化标记数组mark
    mark = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                # 将该元素标记为已使用
                mark[i][j] = 1
                if backtrack(i,j,mark, board, word[1:]) == True:
                    return  True
                else:
                    #backtrack
                    mark[i][j]=0
    return False


# 定义上下左右以及斜方向八个个行走方向
directs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]


def backtrack( i, j, mark, borad, word):
    if len(word) == 0:
        return True
    for direct in directs:
        cur_i = i + direct[0]
        cur_j = j + direct[1]

        if cur_i >= 0 and cur_i < len(borad) and cur_j >= 0 and cur_j < len(borad[0]) and borad[cur_i][cur_j] == word[0]:
            # 如果是已经使用过的元素，忽略
            if mark[cur_i][cur_j] == 1:
                continue
            # 将该元素标记为已使用
            mark[cur_i][cur_j] = 1
            if backtrack(cur_i, cur_j, mark, borad, word[1:]) == True:
                return True
            else:#backtrack
                mark[cur_i][cur_j] = 0

    return False
