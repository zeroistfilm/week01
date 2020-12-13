# https://www.acmicpc.net/problem/9249

A = input()
B=input()

if len(A)>len(B):
    long=A
    short=B
else:
    long=B
    short=A
for i in range(len(long)):
    if short in long:
        break
    short=short[1:]
print(short)


