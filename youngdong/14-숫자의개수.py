# https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())

multi = str(A*B*C)
result=[0,0,0,0,0,0,0,0,0,0]

for i in range(len(multi)):
    a=multi[i]
    for j in range(0,10):
        if multi[i]==str(j):
            result[j]=result[j]+1

for i in result:
    print(i)
