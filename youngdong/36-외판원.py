# # https://www.acmicpc.net/problem/10971
# # OK
#
import sys

N = int(sys.stdin.readline())


#인접행렬 간선 비
pays=[]
for i in range(N):
    pays.append(list(map(int,sys.stdin.readline().split())))

visit=[False for i in range(N)]

current=[]
mincost=9999999999
def dfs(x):
    global cost,mincost
    visit[x]=True
    current.append(x)
    #print(x,'에 방문')

    if len(current) == N:
        cost += pays[x][0]
        if mincost > cost:
            mincost = cost
        cost -= pays[x][0]
        return

    for i in range(N):
        if pays[x][i]!=0 and visit[i]==False:
            cost+=pays[x][i]
            dfs(i)

            visit[i] = False
            cost -= pays[x][i]
            current.pop()


# for i in range(N):
cost=0
dfs(0)
print(mincost)
    # current.pop()
    # visit[i] = False














# import sys
# from itertools import permutations
#
#
# N = int(sys.stdin.readline())
# P=[]
# for i in range(N):
#     P.append(i)
#
# pays=[]
# for i in range(N):
#     pays.append(list(map(int,sys.stdin.readline().split())))
#
# nPr = list(permutations(P, N)) # 순열
# min=0
# for trip in nPr[0:int(len(nPr)/N)]: #어디서 시작해도 싸이클이라 똑같으니 0에서 시작한다고 하면
#     trip=list(trip)
#     trip.append(trip[0])
#     #print(trip)
#     cost=[]
#     for i in range(len(trip)-1): # 24번 반복
#         if pays[trip[i]][trip[i + 1]]==0:
#             break
#         cost.append(pays[trip[i]][trip[i + 1]])
#         # print(f'{trip[i]} to {trip[i + 1]}' )
#         # trip[i] to trip[i+1] 0->1->2->3->0
#     if len(cost)==N:
#         if min==0:
#             min= sum(cost)
#         elif min>sum(cost):
#             min = sum(cost)
#
# print(min)
