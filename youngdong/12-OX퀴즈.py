# https://www.acmicpc.net/problem/8958

N = int(input())

cases=[]
score=0
result=0
for i in range(N):
    cases.append(input())

for case in cases:
    for i in range(len(case)):

        if case[i] =='O':
            score+=1
        elif case[i] == 'X':
            score =0
        result+=score
    print(result)
    score = 0
    result = 0





