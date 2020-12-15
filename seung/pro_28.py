n = int(input())
pos = [0]*n # 퀸의 위치가 열마다 담긴 리스트
flag_a = [False]*n
flag_b = [False]*(2*n-1)
flag_c = [False]*(2*n-1)
count = 0
# 일렬로 행을 만들어주는 함수, pos[i]가 무엇이냐에 따라 다르게 출력될듯.
def put() -> None:
    # for j in range(8):
    for i in range(n):
        # print('◾️' if pos[i]== j else '◽️', end='')
        print(pos[i] , end='')

        # print()
    print()


def set(i: int) -> None:
    global count
    for j in range(n):
        if (not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+(n-1)]):
            pos[i] = j
            if i == n-1:
                # put()
                count += 1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = False
    return count
print(set(0))