# https://www.acmicpc.net/problem/1152

sentence = list(map(str,input().strip().split(' ')))
# 반례 입력 ' '이 있음.. 예외 처리 말고 해결하는 방법이 있을까?
length = len(sentence)
if sentence[0]=='':
    length=0
print(length)