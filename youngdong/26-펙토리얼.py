# https://www.acmicpc.net/problem/10872

N = int(input())
result=1
for i in range(1,N+1):
    result=result*i
print(result)