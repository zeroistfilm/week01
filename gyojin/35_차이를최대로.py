

from itertools import permutations
n = int(input())
test = list(map(int, input().split()))
maximum = 0

for num in list(permutations(test, n)):
    total = 0
    for i in range(n-1):
        total += abs(num[i] - num[i+1])
        maximum = max(total, maximum)

print(maximum)
