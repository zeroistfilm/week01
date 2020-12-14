


a = int(input())
test = map(int, input().split())
# print(sum(map(lambda n: all(n % j for j in range(2,n)) and n>1, test)))

# 풀이 1
cnt = 0
for i in test:
    is_prime = True
    if i <= 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime is True:
        cnt += 1

print(cnt)

# 풀이 2
# check = [True] * a
# m = int(max(test) ** 0.5)
#
# for i in range(2, m+1):
#     if check[i] is True:
#         for j in range(i+1, a):
#             if test[j] % i == 0:
#                 check[j] = False
#
# print(sum(check) - 1)




