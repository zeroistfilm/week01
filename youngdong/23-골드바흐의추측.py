# https://www.acmicpc.net/problem/9020
#
N=int(input())
list=[]
for i in range(N):
    list.append(int(input()))


def idx_prime(n: int) -> list:
    seive = [True] * (n+1)
    for j in range(2, n):
        if seive[j] is True:
            for k in range(j+j, n+1, j): #j=2, 2의 배수는 모두 fasle , 3의 배수는 모두 fasle
                seive[k] = False
    return seive



def goldbach(n:int)->None:
    getprimelist=idx_prime(n)
    index=len(getprimelist)//2 # 중간부터 탐색
    for i in range(index,1,-1): #중간부터 2까지 -1씩
        if getprimelist[n-i] and getprimelist[i]: #N = i + (N-i)
            print(i, n-i)
            break



for i in list:
    goldbach(i)


