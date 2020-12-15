# https://www.acmicpc.net/problem/9663

# 깊이 우선 탐색(DFS, Depth-First Search)

N=int(input())
pos=[0]*N # 열배치
flag_a=[False]*N #행배치
flag_b=[False]*(N*2-1)
flag_c=[False]*(N*2-1)

def put()->None:
    for j in range(N):
        for i in range(N):
            #print(f'{pos[i]:2}',end='')
            print('♖'if pos[i]==j else '☐',end='')
        print()
    print()



cnt=0


def set(i:int)->int:
    global cnt
    for j in range(N):
        if (not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+N-1]): #fasle일때만 실행
            pos[i]=j# 1열에 1개씩 배치
            if i ==N-1:
                #put()
                cnt+=1
            else:
                flag_a[j]=flag_b[i+j]=flag_c[i-j+N-1]=True
                set(i+1)
                flag_a[j]=flag_b[i+j]=flag_c[i-j+N-1]=False   #재귀 호출한 함수가 끝나면 퀸을 J 행에서 제거 해야 한다.


set(0)
print(cnt)