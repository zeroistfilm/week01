import sys
n = int(input())
a = [int(sys.stdin.readline()) for i in range(n)]
print(a)
for i in sorted(a):
	print(i)