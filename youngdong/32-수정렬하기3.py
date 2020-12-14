#https://www.acmicpc.net/problem/10989

N = int(input())

numbers=[]
for i in range(N):
    numbers.append(int(input()))

distribution=[0]*(max(numbers)+1)

for i in range(N):
    distribution[numbers[i]]+=1

for i in range(1,len(distribution)):
    distribution[i]=distribution[i-1]+distribution[i]

result = [0] * len(numbers)

for i in range(N-1,-1,-1): #-1 이면 직전까지인 0까지 간다.
    result[distribution[numbers[i]]-1]=numbers[i]
    distribution[numbers[i]]-=1

for i in result:
    print(i)
