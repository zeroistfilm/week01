

t = int(input())
test = list()

for i in range(t):
    a, b = map(int, input().split())
    test.append([a, b])

for i in range(t):
    print(test[i][0] + test[i][1])
