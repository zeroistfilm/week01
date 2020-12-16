import sys
n = int(sys.stdin.readline())
org_lst = [int(sys.stdin.readline()) for i in range(n)]
# 중복된 수는 없으니 셸 정렬 쓸 수는 있을듯.
def shell_sort(lst):
    lst_len= len(lst)
    interv=1
    while interv < n//9:
        interv = interv*3+1
    while interv > 0:
        for i in range(interv,lst_len):
            j = i-interv
            tmp = lst[i]
            while j>= 0 and lst[j] > tmp:
                lst[j+interv] = lst[j] #h만큼 떨어져있는 원소랑 스위칭
                j -= interv #h만큼 떨어져있는 원소들과 비교해야되서 j-1이 아니라 j-h 원소로 가야된다.
            lst[j+interv] = tmp
        interv = interv // 3
    return lst

def sort3(a,idx1,idx2,idx3):
    if a[idx2] < a[idx1]:
        a[idx2],a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]:
        a[idx3], a[idx2] = a[idx2],a[idx3]
    if a[idx2] < a[idx1]:
        a[idx2],a[idx1] = a[idx1] , a[idx2]
    return idx2

def qsort(lst, left:int, right:int):
    pl = left
    pr = right
    pivot = sort3(lst,pl,(pl+pr)//2, pr)
    x= lst[pivot]

    lst[pivot],lst[pr-1] = lst[pr-1], lst[pivot]
    pl+=1
    pr-=2
    while pl <= pr:
        while lst[pl] < x: pl +=1
        while lst[pr] > x: pr -=1
        if pl<= pr :
            lst[pl],lst[pr] = lst[pr],lst[pl]
            pl+=1
            pr-=1
    if left < pr: qsort(lst,left,pr)
    if pl< right: qsort(lst,pl,right)
    return lst


def quick_sort(lst) -> None:
    return qsort(lst,0,len(lst)-1)


print("----")
for i in quick_sort(org_lst):
    print(i)