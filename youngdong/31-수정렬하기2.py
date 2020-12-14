# https://www.acmicpc.net/problem/2751
# OK

N = int(input())

numbers=[]
for i in range(N):
    numbers.append(int(input()))

h=len(numbers)//2 #칸수
m=2
# 0 4
# 1 4
# 2 4
# 3 4
# 0 2
# 1 2
# 0 1
# print(numbers)
while h>0:
    for i in range(h, N):
        j=i-h
        tmp=numbers[i]
        while j>=0 and numbers[j]>tmp:
            numbers[j+h]=numbers[j]
            j-=h
        numbers[j+h]=tmp
    h//=2

for i in numbers:
    print(i)