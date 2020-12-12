

a = int(input())


def factorial(n: int) -> int:
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


print(factorial(a))
