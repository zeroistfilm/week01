

n = int(input())
w = [list(map(int, input().split())) for i in range(n)]
p = len(w)
visit = [0] * p
minPath = 10000000


#     for i in range(p):
#         start = i
#         totalC = 0
#         visit = [0] * p
#         for j in range(p):
#             if w[i][j] == 0 or visit[j] == 1:
#                 continue
#             cost += w[i][j]
#             visit[j] = 1
#             i = j
#         path = min(cost, path)


def tsp(start: int, pos: int, cost: int):
    global minPath, visit

    # print(start, pos, cost, visit, minPath)

    if pos == start and all(visit) is True:
        minPath = min(cost, minPath)

    for i in range(p):
        if w[pos][i] != 0 and visit[i] != 1:
            # cost += w[pos][i]
            visit[i] = 1
            tsp(start, i, cost + w[pos][i])
            visit[i] = 0


tsp(0, 0, 0)
# minPathList = [0] * n
# for i in range(n):
#     tsp(i, i, 0)
#     minPathList[i] = minPath
#
# print(minPathList)
