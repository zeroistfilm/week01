from typing import MutableSequence
# n번째 패스 때 정렬이 끝났으면 , 그 뒤 패스부터는 돌릴 필요가 없음
# def bubble_sort(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(n-1):
#         exch_cnt = 0
#         for j in range(n-1,i,-1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#                 exch_cnt +=1
#         if exch_cnt == 0:
#             break

# 이미 이전 패스에서 원소 n개가 정렬이 되어있으면, n 이후부터만 정렬하면 됨.
# def bubble_sort(a: MutableSequence)-> None:
#     n = len(a)
#     k = 0
#     while k<n-1:
#         last = n-1
#         for j in range(n-1,k,-1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#                 last = j
#         # last가 for loop 안에서 j를 참조하는게 아니라 위에 n-1을 그대로 들고와서 k가 참조하면, while loop 조건이 false가 되어 루프 종 = 정렬 다했다.
#         k = last
#
x = [6,4,3,7,1,9,8]
# bubble_sort(x)

# 셰이커 정렬
# 홀수 번째에서는 가장 작은 원소를 맨 앞으로 이동(오른쪽 -> 왼쪽), 짝수번째에서는 가장 큰 걸 맨 뒤로 이동(왼쪽 -> 오른쪽)
# def shaker_sort(a: MutableSequence) -> None:
#     left = 0
#     right = len(a)-1
#     last = right
#     while left < right:
#         for j in range(right,left,-1):
#             if a[j-i] > a[j]:
#                 a[j-1], a[j] = a[j],a[j-1]
#                 last = j
#         left = last
#
#         for j in range(left,right):
#             if a[j]> a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
#                 last = j
#         right = last


# 단순선택 정렬
# def selection_sort(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(n-1): # i는 반복문 들어갈 때는 고정이니까 내부 반복문 종료된 시점에 인덱스 i와 min을 바꿀 수 있음
#         min = i
#         for j in range(i+1, n):
#             if a[j] < a[min]:
#                 min =j # 한번 배열을 돌아서 제일 작은 min을 찾는 것.
#         a[i],a[min] = a[min],a[i]
#
# selection_sort(x)

# 단순 삽입정렬(shuttle sort), 이중 반복문을 쓰는 것.
# def insertion_sort(a:MutableSequence) -> None:
#     n = len(a)
#     for i in range(1,n):
#         j = i
#         tmp = a[i] #현재 i로 접근하는 값
#         while j > 0 and a[j-1] > tmp: #j(i랑 같음)가 0보다 크거나(j가 0이되면 배열이 끝), i보다 앞에 있는게 a[i]보다 클 때(작으면 정렬 해야되서)
#             a[j] = a[j-1]
#             j -= 1
#         # 루프가 끝난 다는 건 a[i] 보다 작은게 있다는거고 작은거(j-1) 뒤에 넣어야 함.
#         a[j]= tmp
#
# insertion_sort(x)

# 이진 삽입 정렬
# import bisect
# def binary_insertion_sort(a: MutableSequence) -> None:
#     for i in range(1, len(a)):
#         bisect.insort(a,a.pop(i),0,i)
#
# binary_insertion_sort(x)

# 셸 정렬
# def shell_sort(a:MutableSequence) -> None:
#     n = len(a)
#     h = n//2
#     while h> 0:
#         for i in range(h,n):
#             j = i-h
#             tmp = a[i]
#             while j>= 0 and a[j] > tmp:
#                 a[j+h] = a[j] #h만큼 떨어져있는 원소랑 스위칭
#                 j -= h #h만큼 떨어져있는 원소들과 비교해야되서 j-1이 아니라 j-h 원소로 가야된다.
#             a[j+h] = tmp
#         h = h // 2

# 퀵소트
# def qsort(a: MutableSequence, left:int, right:int)-> None:
#     pl = left
#     pr = right
#     pivot = a[(left+right)//2] #피벗 = 여기서는 가운데원소를 기준으로 둠
#     while pl <= pr:
#         while a[pl] < pivot: pl +=1
#         while a[pr] > pivot: pr -=1
#         if pl<= pr :
#             a[pl],a[pr] = a[pr],a[pl]
#             pl+=1
#             pr-=1
#     if left < pr: qsort(a,left,pr)
#     if pl< right: qsort(a,pl,right)


# def quick_sort(a:MutableSequence) -> None:
#     qsort(x,0,len(a)-1)
#
# quick_sort(x)

# 병합정렬
def merge_sort(a:MutableSequence) -> None:

    def _merge_sort(a:MutableSequence, left:int, right:int) -> None:
        if left < right:
            center = (left+right) // 2
            _merge_sort(a,left,center)
            _merge_sort(a,center+1,right)

            p = j =0
            i = k =left

            while i <= center:
                buff[p] = a[i]
                p+=1
                i+=1

            while i<= right and j<p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j+=1
                else:
                    a[k] = a[i]
                    i+=1
                k+=1

            while j<p:
                a[k] = buff[j]
                k+=1
                j+=1

    n = len(a)
    buff = [None]*n
    _merge_sort(a,0,n-1)

    del buff


x = [5,8,4,2,6,1,3,9,7]
merge_sort(x)