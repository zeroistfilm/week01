

t = int(input())
test = list(input() for i in range(t))

result = sorted(set(test), key=lambda x: (len(x), x))
print('\n'.join(result))
