# https://www.acmicpc.net/problem/1181

#  ㄴ길이 리스트, 분포리스
import sys

N = int(sys.stdin.readline())

words=[]
for i in range(N):
    A=sys.stdin.readline()
    if not A[:-1] in words:
        words.append(A[:-1]) #리스트에 단어 넣기

wordslen=[]
for i in range(len(words)):
    wordslen.append(len(words[i])) #길이 리스트 만들기

arranged=[None]*(max(wordslen)+1) #


tmp=[]
for i in range(len(words)):
    if arranged[wordslen[i]]==None:
        arranged[wordslen[i]]=words[i]

    else:
        tmp.append(words[i])

        if str(type(arranged[wordslen[i]]))=="<class 'list'>":
            for j in range(len(arranged[wordslen[i]])):
                tmp.append(arranged[wordslen[i]][j])

        else:
            tmp.append(arranged[wordslen[i]])



        tmp.sort()
        del arranged[wordslen[i]]
        arranged.insert(wordslen[i],tmp)
        tmp=[]

for i in arranged:
    if not i==None:
        if str(type(i))=="<class 'list'>":
            for j in i:
                print(j)
        else:
            print(i)
