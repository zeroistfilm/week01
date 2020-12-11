# https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())

# a = 472
# b = 385

print(int(a*(b%10)))
print(int(a*(b%100-b%10)/10))
print(int(a*(b%1000-b%100)/100))
print(int(a*b))