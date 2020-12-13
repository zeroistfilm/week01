# https://www.acmicpc.net/problem/9663

# 깊이 우선 탐색(DFS, Depth-First Search)

N= int(input())

vx=[None]*16
vy=[None]*16


def NQueen(N,y,x):

    for i in range(y):
        if y==vy[i]: return 0
        if x == vx[i]: return 0
        if abs(y-vy[i])==abs(x-vx[i]): return 0


    if y==N-1:
        #말단에서 퀸 배열이 성공적인
        return 1

    vy[y]=y
    vx[y]=x

    solution =0
    for i in range(N):
        solution += NQueen(N,y+1,i)
    return solution


solution=0
for i in range(N):
    solution += NQueen(N,0,i)

print(solution)