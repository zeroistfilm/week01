# https://www.acmicpc.net/problem/10819
# OK

import sys
from itertools import permutations


N = int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
nPr = permutations(A, N) # 순열
a=[]
max=0
# print(len(list(nPr)))
for combi in list(nPr):
    combi=list(combi)
    for i in range(N-1):
        a.append(abs(combi[i]-combi[i+1]))

    # print(a,sum(a))

    if max==0:
        max=sum(a)
    elif max<sum(a):
        max=sum(a)
    a=[]
print(max)
