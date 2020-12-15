#https://www.acmicpc.net/problem/10989
import sys
#도수정렬

N = int(sys.stdin.readline())

numbers=[0]*10001
for i in range(N):
    numbers[int(sys.stdin.readline())]+=1


for i in range(len(numbers)):
    if not numbers[i] ==0:
        # print(f'{i} in numbers: {numbers[i]}')
        if numbers[i]>1:
            for j in range(numbers[i]):
                print(str(i))
        else:
            print(str(i))

