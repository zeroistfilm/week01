

n = int(input())
test = [list(map(int, input().split())) for i in range(n)]
ans = 1
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def min_max_of(p: list) -> list:
    minimum = p[0][0]
    maximum = p[0][0]
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] < minimum:
                minimum = p[i][j]
            if p[i][j] > maximum:
                maximum = p[i][j]
    return [minimum, maximum]


def safe_area(row: int, col: int, height: int):

    visit[row][col] = True

    for i in range(4):
        nextRow = row + move[i][0]
        nextCol = col + move[i][1]

        if (0 <= nextRow < n) and (0 <= nextCol < n):
            if (test[nextRow][nextCol] - height > 0) and not visit[nextRow][nextCol]:
                safe_area(nextRow, nextCol, height)


a = min_max_of(test)[0]
b = min_max_of(test)[1]

for rain in range(a, b):
    # visit = [[False] * n] * n
    visit = [[False] * n for _ in range(n)]
    safezone = 0
    for i in range(n):
        for j in range(n):
            if (test[i][j] > rain) and not visit[i][j]:
                safe_area(i, j, rain)
                safezone += 1
    ans = max(safezone, ans)

print(ans)

