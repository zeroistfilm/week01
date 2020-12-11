

tempList = list()
for i in range(9):
    tempList.append(int(input()))

maximum = tempList[0]
for i in range(9):
    if tempList[i] > maximum:
        maximum = tempList[i]

print(maximum)
print(tempList.index(maximum) + 1)
