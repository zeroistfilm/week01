

dwarf = sorted(list(int(input()) for i in range(9)))
age_diff = sum(dwarf) - 100

# # for문
# for i in range(9):
#     for j in range(8, i, -1):
#         if dwarf[i] + dwarf[j] == age_diff:
#             a = dwarf[i]
#             b = dwarf[j]
#             break
#
# dwarf.remove(a)
# dwarf.remove(b)
# for age in dwarf:
#     print(age)


# combinations
from itertools import combinations

for age in list(combinations(dwarf, 7)):
    if sum(age) == 100:
        for i in age:
            print(i)
        break
