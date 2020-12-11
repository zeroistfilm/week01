# https://www.acmicpc.net/problem/4344

N = int(input())

scores=[]
for i in range(N):
    score=list(map(int,input().split(' ')))
    scores.append(score)

for score in scores:
    studentsNumber = score[0]
    average = sum(score[1:])/len(score[1:])
    higherNumber = len([x for x in score[1:] if x>average])
    print(f'{higherNumber/studentsNumber*100:.3f}%')

