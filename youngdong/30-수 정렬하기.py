# https://www.acmicpc.net/problem/2750

N = int(input())

numbers=[]
for i in range(N):
    numbers.append(int(input()))



for i in range(1,len(numbers)):
    j=i
    tmp=numbers[i] #임시로 꺼냄
    while j>0 and numbers[j-1]>numbers[j]: # 앞에 있게 크면
        numbers[j]=numbers[j-1]
        numbers[j-1]=tmp
        j-=1


for i in numbers:
    print(i)
