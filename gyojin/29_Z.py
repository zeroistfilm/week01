

def Zfind(n: int, row: int, col: int, cnt: int):

    if n == 1:
        # if row == 0 and col == 0:
        #     cnt += 1
        if row == 0 and col == 1:
            cnt += 1
        if row == 1 and col == 0:
            cnt += 2
        if row == 1 and col == 1:
            cnt += 3
        return cnt

    else:
        quat = 2 ** (n - 1)
        # 1사분면
        if row < quat and col < quat:
            return Zfind(n - 1, row, col, cnt)
        # 2사분면
        if row < quat <= col:
            cnt += quat**2
            return Zfind(n - 1, row, col-quat, cnt)
        # 3사분면
        if row >= quat > col:
            cnt += quat**2 * 2
            return Zfind(n - 1, row-quat, col, cnt)
        # 4사분면
        if row >= quat and col >= quat:
            cnt += quat**2 * 3
            return Zfind(n - 1, row-quat, col-quat, cnt)


a, r, c = map(int, input().split())
print(Zfind(a, r, c, 0))

