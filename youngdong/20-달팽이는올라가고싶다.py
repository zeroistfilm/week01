# https://www.acmicpc.net/problem/2869
import math

A,B,V = map(int,input().split())
print(math.ceil((V-A)/(A-B))+1)