# https://www.acmicpc.net/problem/1978

N=int(input())
M=list(map(int,input().split()))
list=[]


def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
counts=0
for i in M:
    if(is_prime(i)):
        counts+=1

print(counts)
