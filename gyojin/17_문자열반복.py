

a = int(input())
test = list()
for i in range(a):
    test.append(list(map(str, input().split())))

for i in range(a):
    r = int(test[i][0])
    s = test[i][1]
    for j in range(len(s)):
        print(s[j] * r, end='')
    print()

