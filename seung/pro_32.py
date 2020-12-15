import sys
n = int(sys.stdin.readline())
org_lst = [sys.stdin.readline().split() for i in range(n)]

lst = sorted(org_lst,key=len)
print(lst)

