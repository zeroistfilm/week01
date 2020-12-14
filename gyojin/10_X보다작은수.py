

n, x = map(int, input().split())
a = map(int, input().split())
tempList = list(a)

for i in range(n):
    if tempList[i] < x:
        print(tempList[i], end=' ')
