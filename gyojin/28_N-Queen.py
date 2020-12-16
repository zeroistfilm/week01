# https://www.acmicpc.net/problem/9663

n = int(input())

pos = [0] * n
li = [[0] * n] * n
flag_a = [False] * n
flag_b = [False] * (n*2-1)
flag_c = [False] * (n*2-1)
cnt = 0


# def put() -> None:
#     for i in range(n):
#         for j in range(n):
#             li[i][j] = pos[i]
#         # print(f'{pos[i]:3}', end='')


def set_queen(i: int) -> None:
    global cnt
    # i열에 퀸 배치하기
    for j in range(n):
        if (    not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + (n-1)]):
            pos[i] = j      # 퀸을 j행에 배치
            if i == n-1:
                cnt += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = True
                set_queen(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = False


set_queen(0)
print(cnt)
