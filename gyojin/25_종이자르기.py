

c, r = map(int, input().split())
t = int(input())
tmpR = [0]
tmpC = [0]

for i in range(t):
    a, b = input().split()
    if a == '0':
        tmpR.append(int(b))
    else:
        tmpC.append(int(b))

tmpR.sort()
tmpC.sort()
tmpR.append(r)
tmpC.append(c)

maxR = 0
for i in range(1, len(tmpR)):
    if maxR < tmpR[i] - tmpR[i-1]:
        maxR = tmpR[i] - tmpR[i-1]

maxC = 0
for i in range(1, len(tmpC)):
    if maxC < tmpC[i] - tmpC[i-1]:
        maxC = tmpC[i] - tmpC[i-1]

print(maxR * maxC)
