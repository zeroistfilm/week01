# https://www.acmicpc.net/problem/2503


from itertools import permutations

#
N = int(input())
baseballs=[]
for i in range(N):
    baseballs.append(list(map(int,input().split())))


combis=permutations([i for i in range(1,10)],3)
for combi in combis:
    print(combi)

baseballs.sort(key=lambda x:x[1],reverse=True) #스트라이크순으로 정렬o
#가능한 조합을 찾아서 새롭게 담아 줘야한다.


onestrike = list(baseball for baseball in baseballs if baseball[1]==1)
twostrike = list(baseball for baseball in baseballs if baseball[1]==2)


for i in range(len(onestrike)):
    first= twostrike[0]//100
    second=twostrike[0]//10
    thrd=twostrike[0]%10
    print(first,second,thrd)


