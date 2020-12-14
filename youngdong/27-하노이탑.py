# https://www.acmicpc.net/problem/1914

N = int(input())

def hanoi(num, frm, to, other):
    if num == 0: return 0
    hanoi(num - 1, frm, other, to)  # 하나 적은 원반을 목적지가 아닌 다른 곳으로
    print(f'{frm} {to}')
    hanoi(num - 1, other, to, frm)  # 다른곳에


def hanoicount(N):
    if N == 1:
        return 1

    return hanoicount(N - 1) * 2 + 1

print(hanoicount(N))
if N % 2 == 0:
    to = 2
    other = 3
else:
    to = 3
    other = 2
if N<20:
    hanoi(N, 1, to, other)
