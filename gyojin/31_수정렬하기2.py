

# 퀵 정렬
def qsort(a: list, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)


t = int(input())
test = list(int(input()) for i in range(t))
qsort(test, 0, t-1)
for num in test:
    print(num)
