# https://www.acmicpc.net/problem/2309
# OK

from itertools import combinations

heights=[]
for i in range(9):
    heights.append(int(input()))

a=[]
for i in list(combinations(heights,7)):
    a.append(list(i))

for i in a:
    if sum(i)==100:
        i.sort()
        for j in i:
            print(j)
        break
