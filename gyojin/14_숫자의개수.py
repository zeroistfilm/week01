

a = int(input())
b = int(input())
c = int(input())

total = str(a * b * c)
test = list(range(10))

for i in range(len(test)):
    cnt = 0
    for j in range(len(total)):
        if int(total[j]) == test[i]:
            cnt += 1
    print(cnt)
