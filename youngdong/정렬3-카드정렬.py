# # https://www.acmicpc.net/problem/1715

# 힙은 작은 순서대로 정렬된다
import heapq

N = int(input())

heap=[]
for i in range(N):
    data=int(input())
    heapq.heappush(heap,data)

result=0

while len(heap)!=1: #원소가 하나 남을때 까지
    one=heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value=one+two
    result +=sum_value
    heapq.heappush(heap,sum_value)

print(result)