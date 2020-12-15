# https://www.acmicpc.net/problem/2468
import sys
import copy
sys.setrecursionlimit(100000)



N = int(sys.stdin.readline())
land=[]
for i in range(N):
    land.append(list(map(int,sys.stdin.readline().split())))


# land=[a,b,c,d,e]
# landExtende=[a,b,c,d,e]
#상하단에 빈칸을 넣어줌
# land.insert(0,[0]*N)
# land.insert(N+1,[0]*N)
# for i in range(N+2):
#     land[i].insert(0, 0)
#     land[i].insert(N+1, 0)

count=0

countlist=[]

def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    if land[x][y]>0 :
        land[x][y]=0 #방문체크
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False

# for m in land:
#     print(m)

count = 0
original = copy.deepcopy(land)

for i in range(1,max(map(max, land))):# 가장 높은 곳까지 물이 찰 때
    land = copy.deepcopy(original)
    # print(i)
    for j in range(N):
        for k in range(N):
            if land[j][k] <= i:
                land[j][k] = land[j][k]-i

    # for m in land:
    #     print(m)

    # #물에 잠기지 않는 안전영역 체크
    # print(len(land)) #5
    for j in range(len(land)):
        for k in range(len(land)): #완전 탐색

            if dfs(j,k)==True:
                count+=1
            pass

    # for m in land:
    #     print(m)
    # print('=================')
        # 물에 잠긴 땅 출력하는 코드

    countlist.append(count)
    count=0

print(max(countlist))





