

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


# 단순 삽입 정렬
def insertion_sort(a: list):
    n = len(a)
    for i in range(1, n):
        tmp = a[i]
        j = i
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

# 검색 범위의 맨 앞 원소 index
# 이진 삽입 정렬
def binary_insertion_sort(a: list):
    n = len(a)
    for i in range(n):
        key = a[i]
        pl = 0                              # 검색 범위의 맨 앞 원소 index
        pr = i - 1                          # 검색 범위의 맨 뒤 원소 index

        while True:
            pc = (pl + pr) // 2             # 검색 범위의 가운데 원소 index
            if a[pc] == key:                # 검색 성공
                break
            elif a[pc] > key:
                pl = pc + 1                 # 검색 범위를 뒤쪽 절반으로 좁힘
            else:
                pr = pc - 1                 # 검색 범위를 앞쪽 절반으로 좁힘
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1 # 삽입해야 할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key


# 셸 정렬
def shell_sort(a: list):
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 3

t = int(input())
test = list(int(input()) for i in range(t))
shell_sort(test)
for num in test:
    print(num)
