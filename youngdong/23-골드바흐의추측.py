# https://www.acmicpc.net/problem/9020
#
# N=int(input())
# list=[]
# for i in range(N):
#     list.append(int(input()))


def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

print(is_prime(3))



