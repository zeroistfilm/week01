

def idx_prime(n: int) -> list:
    seive = [True] * (n+1)
    m = int(n ** 0.5) + 1
    for j in range(2, n):
        if seive[j] is True:
            for k in range(j+j, n+1, j):
                seive[k] = False
    return seive


def goldbach(n: int) -> None:
    li = idx_prime(n)
    idx = len(li) // 2
    for i in range(idx, 1, -1):
        if li[n-i] and li[i] is True:
            print(i, n-i)
            break

        # for j in range(idx, -1, -1):
        #     if li[i] + li[j] == n:
        #         print(f'{li[i]} {li[j]}')
        #         break
        #     if li[i] + li[j] < n:
        #         break


t = int(input())
test = list(int(input()) for i in range(t))
for num in test:
    goldbach(num)

