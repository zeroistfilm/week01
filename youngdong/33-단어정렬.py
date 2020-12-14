# https://www.acmicpc.net/problem/1181

# 중복은 허용하지 않고 리스트에 담기
# 길이가 짧은 것으로 정렬 -
#  ㄴ길이 리스트, 분포리스



N = int(input())

words=[]
for i in range(N):
    A=input()
    if not A in words:
        words.append(A)
maxlen=''
for i in words:
    if maxlen=='':
        maxlen = len(i)
    if maxlen<len(i):
        maxlen = len(i)

print(maxlen)

dist=[0]*maxlen

for i in range(1,len(words)+1):
    print(words[i-1])
    dist[len(words[i-1])-1]+=1

for i in range(1,maxlen):
    dist[i]+=dist[i-1]

tmp=[]
for i in range(len(words)-1,-1,-1)
    dist[len(words[i])]-=1
    tmp
print(dist)




#
# lenthofwords=[0]*len(words)
#
# for i in range(len(words)):
#     lenthofwords[i]=len(words[i])
# print(lenthofwords)
#
# sorted=[None]*(max(lenthofwords))
#
#
# for i in range(len(words)):
#     if sorted[len(words[i])-1]==None:
#         sorted[len(words[i])-1]=words[i]
#     else:
#
#         print(words[i],' vs ',sorted[len(words[i]) - 1])
#         j=0
#         while len(words[i])>j:
#
#             print(words[i][j],' vs ',sorted[len(words[i]) - 1][j])
#             if words[i][j]==sorted[len(words[i]) - 1][j]:
#                 pass
#             else:
#                 print(ord(words[i][j]),'vs',ord(sorted[len(words[i]) - 1][j]))
#
#
#                 if ord(words[i][j])>ord(sorted[len(words[i]) - 1][j]): #새로운게 더 크면
#                     sorted.insert(i,words[i])
#                     print(sorted)
#                 else: #새로운게 더 작다
#                     sorted.insert(i-1, sorted[len(words[i]) - 1])
#                     print(sorted)
#
#             j+=1
#
#
# print(sorted)