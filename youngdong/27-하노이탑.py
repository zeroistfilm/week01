# https://www.acmicpc.net/problem/1914

N = int(input())

def hanoi(num, x, y):
    if num == 0: return 0
    hanoi(num - 1, x, 6-x-y)  # 하나 적은 원반을 목적지가 아닌 다른 곳으로
    print(f'{x} {y}')
    hanoi(num - 1, 6-x-y, y)  # 다른곳에


def hanoicount(N):
    if N == 1:
        return 1

    return hanoicount(N - 1) * 2 + 1

print(hanoicount(N))

if N<=20:
    hanoi(N, 1, 3)
