# https://www.acmicpc.net/problem/1074


N, r, c = map(int, input().split())


def check_position(N,r,c):

    sizelength = 2 ** (N)
    Matrixsize=sizelength*sizelength


    if sizelength==1:
        return 0
    if r < (sizelength // 2):
        if c < (sizelength // 2):
            Q = 1
            r=r
            c=c
        else:
            Q = 2
            r=r
            c=c-sizelength // 2
    else:
        if c < (sizelength// 2):
            Q = 3
            r=r-sizelength // 2
            c=c
        else:
            Q = 4
            r = r - sizelength // 2
            c = c - sizelength // 2

    quadrantsize = int(Matrixsize / 4)
    count.append(quadrantsize * (Q-1))
    check_position(N-1, r,c)



count=[]
check_position(N,r,c)
print(sum(count))

#
# for i in range(len(M)):
#     print(M[i])

