

a = input()

if len(a) < 3:
    print(int(a))
else:
    cnt = 99
    for k in range(100, int(a)+1):
        num = list(map(int, str(k)))
        # if lambda n: all(num[n] - num[n+1] == num[n+1] - num[n+2] for n in range(len(a)) and n < len(a)-2):
        if num[0] - num[1] == num[1] - num[2]:
            cnt += 1
    print(cnt)

