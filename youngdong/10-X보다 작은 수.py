# https://www.acmicpc.net/problem/10871

N,X = map(int,input().split(' '))

A = list(map(int,input().split(' ')))

for number in A:
    if X>number:
        print(number, end=' ')