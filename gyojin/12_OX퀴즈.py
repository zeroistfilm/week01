

a = int(input())
test = list()

for i in range(a):
    test.append(input())


for i in range(a):
    cnt = 0
    score = 0
    for j in range(len(test[i])):
        if test[i][j] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
