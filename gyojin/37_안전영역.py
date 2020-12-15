

n = int(input())
test = [list(map(int, input().split())) for i in range(n)]
tmp = test
maxH = 0

for i in range(n):
    for sct in test[i]:
        maxH = max(max(sct), maxH)


