# https://www.acmicpc.net/problem/4344

N = int(input())

scores=[]
for i in range(N):
    score=list(map(int,input().split(' ')))
    scores.append(score)

for score in scores:
    studentsNumber = score[0]
    average = sum(score[1:])/len(score[1:])

