

a = int(input())
test = list()

for i in range(a):
    test.append(map(int, input().split()))

for i in range(a):
    temp = list(test[i])
    total = 0
    avg = 0
    cnt = 0
    stu = temp[0]

    for j in range(1, stu+1):
        total += temp[j]

    avg = total / stu
    for j in range(1, stu+1):
        if temp[j] > avg:
            cnt += 1

    print('%.3f' % round((cnt / stu) * 100, 3) + '%')

