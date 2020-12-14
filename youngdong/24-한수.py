# https://www.acmicpc.net/problem/1065
# OK
M=input()

N=[]
count=0

if int(M)<100:
    count = M
else:
    count = 99
    for a in range(1,int(M)+1):

        a=str(a)
        for i in range(1,len(a)): #자리수 나누기
            diff = int(a[i])-int(a[i-1])
            N.append(diff)

        if len(N)>1:
            if N[0]==N[1]:
                # print(N)
                count+=1
        N=[]
print(count)
