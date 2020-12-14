

a, b = map(str, input().split())
a2 = ''
b2 = ''

for i in reversed(range(3)):
    a2 += a[i]
    b2 += b[i]

print(max(int(a2), int(b2)))
