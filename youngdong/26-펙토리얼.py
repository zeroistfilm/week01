# https://www.acmicpc.net/problem/10872

N = int(input())

def factorial(N):
    if N==1:
        return 1
    return N * factorial(N-1)

print(factorial(N))