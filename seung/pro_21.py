import sys,math
a,b,v = map(int, sys.stdin.readline().split())
day = math.ceil((v-a)/(a-b))+1
print(int(day))
