# https://www.acmicpc.net/problem/1110

N = int(input())
count=0

origin=N
def slice(N,count):

    front = N//10
    end = N%10

    if N==origin and count!=0:
        print(count)
        return
    count+=1
    slice(int (str(end)+str((front+end)%10)),count)

slice(N,count)


