
import heapq

nums = [4, 1, 7, 3, 8, 5,9,10,11,12,13,14,15,16]
heap = []
heap2 = []
heap3 = []
for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
  heapq.heappush(heap2, (num))
  heapq.heappush(heap3, (-num))

while heap:
  print(heapq.heappop(heap)[1])  # index 1
  print(heapq.heappop(heap2))