a,b = map(int, input().split())
ans_list = list(map(int,input().split()))
for item in ans_list:
    if b > item:
        print(item, end=' ')