import sys, math

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))  # 소수 판별 리스트
print("---")
count = 0


def prime_check(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:  # 짝수면 안 됨.
        return False

    if num >=3:
        std = math.sqrt(num)
        print(math.ceil(std))
        for i in range(3, math.ceil(std)+1, 2):
            print("i:",i)
            if num % i == 0:
                return False
    return True


for i in range(n):
    print(prime_check(lst[i]))
    if prime_check(lst[i]) == True:
        count += 1

print(count)