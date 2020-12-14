
n = int(input())
num = list(int(input()) for i in range(n))


# 버블 정렬
def bubble_sort(a: list) -> None:
    seq = len(a)-1
    for i in range(seq):
        for j in range(seq, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


# 쉐이커 정렬
def shaker_sort(a: list) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for i in range(right, left, -1):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                last = i
        left = last

        for i in range(left, right):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                last = i
        right = last


# bubble_sort(num)
shaker_sort(num)
for k in num:
    print(str(k))
