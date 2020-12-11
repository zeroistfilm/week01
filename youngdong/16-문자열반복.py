# https://www.acmicpc.net/problem/2675

N = int(input())

cases=[]
for i in range(N):
    M, string = map(str,input().split(' '))
    cases.append([int(M), string])

result=''
for case in cases:
    M=case[0]
    string=case[1]
    for i in range(len(string)):
        # print(string[i]*M,end='')
        result +=string[i]*M
    print(result)
    result=''