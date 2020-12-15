
import sys
n = int(sys.stdin.readline())
# test = [int(input()) for _ in range(n)]
# tmp = [0 for _ in range(max(test)+1)]


f = [0] * 10001
for i in range(n):
    f[int(sys.stdin.readline())] += 1

for i in range(len(f)):
    if f[i] != 0:
        for j in range(f[i]):
            print(i)



# b = [0] * n
# for i in range(n):
#     f[test[i]] += 1

# for i in range(1, len(f)):
#     f[i] += f[i-1]
# for i in range(n-1, -1, -1):
#     f[test[i]] -= 1
#     b[f[test[i]]] = test[i]
#
# for i in range(n):
#     print(b[i])



