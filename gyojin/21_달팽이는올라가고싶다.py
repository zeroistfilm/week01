

a, b, v = map(str, input().split())
a = int(a)
b = int(b)
v = int(v)
pos = 0
day = 1

while pos < v:
    pos += a
    if pos >= v:
        print(day)
        break
    else:
        pos -= b
        day += 1
