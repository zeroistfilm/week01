# https://www.acmicpc.net/problem/1074


N, r, c = map(int, input().split())

M = [[0 for i in range(2 ** (N))] for j in range(2 ** (N))]


def check_position(M,r,c):
    if len(M)==1:
        return 0
    if r < (len(M) // 2):
        if c < (len(M) // 2):
            Q = 1
        else:
            Q = 2
    else:
        if c < (len(M) // 2):
            Q = 3
        else:
            Q = 4
    totalsize, quadrantsize = get_size(M)


    count = quadrantsize * Q




    return Q,count-1



def get_size(M):
    totalsize = len(M[0]) * len(M[0])
    quadrantsize = int(totalsize / 4)
    return totalsize,quadrantsize
    # postion check


get_size(M)
print(check_position(M,r,c))
for i in range(len(M)):
    print(M[i])

