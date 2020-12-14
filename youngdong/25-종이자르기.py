# https://www.acmicpc.net/problem/2628
# OK
size = list(map(int, input().split()))
times = int(input())
methods = []
for i in range(times):
    methods.append(list(map(int, input().split())))

area = int(size[0] * size[1])

row=[]
columns=[]
row.insert(0, 0)
columns.insert(0, 0)
for method in methods:
    if method[0] == 1:  # split column
        row.append(method[1])
    elif method[0] == 0:  # split row
        columns.append(method[1])

row.append(size[0])
columns.append(size[1])
row.sort()
columns.sort()
# print(row)
# print(columns)

diffrow=[]
diffcolumns=[]
for i in range(1,len(row)):
    diffrow.append(row[i]-row[i-1])
for i in range(1,len(columns)):
    diffcolumns.append(columns[i]-columns[i-1])
# print(diffrow)
# print(diffcolumns)

area=[]
for i in diffrow:
    for j in diffcolumns:
        area.append(i*j)
print(max(area))

