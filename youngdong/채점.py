# 저도 중복순열의 개념으로 문제를 풀었습니다.
#

from itertools import product

T = int(input())
base = [1,2,3]


for i in range(T):
    result = []
    n = int(input())
    for j in range(1, n+1):
        for one in product(base, repeat=j):
            if sum(one) == n:
                result.append(one)

    print(len(result))