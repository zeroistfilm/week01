

# a, b = map(int, input().split("/n"))

a = int(input())
b = int(input())

print(a * (b % 10))
print(a * (b // 10 % 10))
print(a * (b // 100))
print(a * b)


