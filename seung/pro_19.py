# a, b = map(int, input().split())
#
# print(a,b)
# def reverse(num):
#     rev_num = 0
#     while (num > 0):
#         remainder = num % 10  # 바뀌는 수 첫자리부터 됨.
#         rev_num = rev_num * 10 + remainder
#         num = num // 10
#     return rev_num
#
#
# print(max(reverse(a), reverse(b)))

a, b = map(int, input().split())
revr_num = 0
def reversed(num):
    global revr_num   # 재귀함수기 때문에 함수 밖에서 선언해야 리셋이 안된다.
    if (num > 0):
        remainder = num % 10
        revr_num = (revr_num * 10) + remainder
        reversed(num // 10)
   return revr_num

revr_num1 = reversed(a)
revr_num = 0
revr_num2 = reversed(b)
print(max(revr_num1, revr_num2))