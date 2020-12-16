# https://www.acmicpc.net/problem/9249
import sys
#
# A=sys.stdin.readline()
# B=sys.stdin.readline()
A='yeshowmuchiloveyoumydearmotherreallyicannotbelieveit'
B='yeaphowmuchiloveyoumydearmother'

list=[[0 for i in range(len(A))] for i in range(len(B))]


for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            list[j][i]=1

# for i in list:
#     print(i)

count=0
output=[]
def find_str(i,j): #i=x j=y
    global count,x,y
    # print(j,len(B),i,len(A))
    if j >= len(B)-1 or i >= len(A)-1:
        return 0

    if list[j + 1][i + 1]==0 :
        return 0

    if list[j + 1][i + 1]==1:
        count+=1
        find_str(i+1, j+1)
    output.append([y,count])
    #print('index',x,y,'length of word: ',count)

    count=0

for i in range(len(A)):
    for j in range(len(B)):
        global x,y
        x=i
        y=j
        find_str(i, j)

max=0
index=0
for i in range(len(output)):
    if max==0:
        max=output[i][1]
        index = output[i][0]
    if max<output[i][1]:
        max = output[i][1]
        index = output[i][0]

print(max+1)
print(B[index:max+index+1])
