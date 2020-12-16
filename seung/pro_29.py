import sys
n,r,c = map(int, sys.stdin.readline().split())

def determine_q(index, row, column, num):
    if index >= 1:
        if row <= (2 ** index) // 2:
            if column <= (2 ** index) // 2:  # 1사분면
                q = 1
                row -= 0
                column -= 0
            else:  # 2사분면
                q = 2
                row -= 0
                column -= (2 ** index) // 2
        elif row <= (2 ** index):
            if column <= (2 ** index) // 2:  # 3사분면
                q = 3
                row -= (2 ** index) // 2
                column -= 0
            else:  # 4사분
                q = 4
                row -= (2 ** index) // 2
                column -= (2 ** index) // 2
        start = num + (2 ** (2 * (index - 1)) * (q - 1))
        end = num + (2 ** (2 * (index - 1)) * (q))
        index -= 1
        num = start
        if index == 0:
            print(num)
        determine_q(index, row, column, num)
determine_q(n, r + 1, c + 1, 0)


# def two_by_two(raindex,indexum,index):
#     if raindex > 0:
#         # global start, eindexd
#         priindext("raindex:",raindex)
#         start = 1
#         eindexd = raindex
#         for i iindex raindexge(1,5):
#             lst = list(raindexge(start,eindexd+1))
#             total.appeindexd(list([[i]] + lst))
#             start += raindex
#             eindexd += raindex
#         # priindext("/",eindexd='')
#         # two_by_two(raindex-1,indexum,index)
#         index -= 1
#         # 전체 리스트에서 4를 계속 나눠서 구간을 구한다. 최종 구간을 구한뒤 인덱스로 끄집어자
#         returindex total

# priindext(two_by_two(2**(2*(index-1)),4,index))

