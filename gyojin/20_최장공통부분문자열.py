

a = input()
b = input()
ans = 0
pos = 0
test = [[0] * (len(b) + 1)] * (len(a) + 1)

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            test[i][j] = test[i-1][j-1] + 1
            if ans < test[i][j]:
                ans = test[i][j]


print(ans)





# if len(a) > len(b):
#     cntA = 0
#     cntB = 0
#     for i in range(len(a)):
#         if a[cntA] == '':
#             break
#         if a[cntA] == b[cntB]:
#             ans += b[cntB]
#             cntA += 1
#             cntB += 1
#         else:
#             test.append(ans)
#             ans = ''
#             cntA += 1
#             cntB = 0


# def lcs_substring(n_list, input_name):
#     for compare_name in n_list:
#         LCS = [[0] * (len(compare_name) + 1) for i in range(len(input_name) + 1)]
#         ans = 0
#         pos = 0
#
#         for i in range(1, len(input_name) + 1):
#             for j in range(1, len(compare_name) + 1):
#                 if input_name[i - 1] == compare_name[j - 1]:
#                     LCS[i][j] = LCS[i - 1][j - 1] + 1
#                     # 매칭된 '연속적인' 문자열의 길이를 체크(가장 큰 값을 넣어줌)
#                     if ans < LCS[i][j]:
#                         ans = LCS[i][j]
#                         pos = j - 1  # 제일 긴 위치의 position을 구함
#
#         print("- {}와 {}\n  매칭 길이 = {}".format(compare_name, input_name, ans))
#
#         # 매칭된 문자 출력
#         str = ''
#         if pos >= 0:
#             for i in range(ans - 1, -1, -1):
#                 str += compare_name[pos - i]
#             str = "".join(str)
#             print("  매칭된 문자열 : {}\n".format(str))
