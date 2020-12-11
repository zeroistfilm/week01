import heapq

ans_list = []
for i in range(9):
    ans_list.append(int(input()))
print(heapq.nlargest(1,ans_list)[0])
print(ans_list.index(heapq.nlargest(1,ans_list)[0]+1))