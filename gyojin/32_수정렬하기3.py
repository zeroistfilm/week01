

n = int(input())
test = [int(input()) for _ in range(n)]
tmp = [0 for _ in range(max(test)+1)]

for i in range(n):
    x = test[i]
    tmp[x] += 1

for i in range(len(tmp)):
    if tmp[i] != 0:
        for j in range(tmp[i]):
            print(i)

