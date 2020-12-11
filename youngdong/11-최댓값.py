# https://www.acmicpc.net/problem/2562

numbers=[]
for i in range(1,10):
    a = int(input())
    numbers.append(a)

print(max(numbers))
print(numbers.index(max(numbers))+1)