# https://www.acmicpc.net/problem/18310

N = int(input())

homes=list(map(int,input().split()))

homes.sort()
print(homes)

print((homes[(N-1)//2]))