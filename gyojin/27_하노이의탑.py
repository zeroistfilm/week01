

def hanoi(no: int, x: int, y: int) -> None:
    if no > 1:
        hanoi(no-1, x, 6-x-y)

    print(f'{x} {y}')

    if no > 1:
        hanoi(no-1, 6-x-y, y)


n = int(input())
print(2**n - 1)
if n <= 20:
    hanoi(n, 1, 3)

