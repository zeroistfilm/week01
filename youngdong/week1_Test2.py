# https://www.acmicpc.net/problem/9095


from itertools import product

#중복 순열을 사용한 풀이
N=int(input())

numbers=[]
for i in range(N):
    numbers.append(int(input()))

for N in numbers:
    num=[1,2,3]
    count=0
    for i in range(1,N,):
        per=list(product(num,repeat=i))
        for j in per:
            if sum(j)==N:
                count+=1
                print(j)

    print(count+1)