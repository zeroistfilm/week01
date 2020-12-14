import sys
hori_total,verti_total = map(int, sys.stdin.readline().split())
cut_count = int(input())
hori_lst = []
verti_lst = []
total_lst = sorted([list(map(int, sys.stdin.readline().split())) for i in range(cut_count)])

for i,v in total_lst:
    if i == 0:
        hori_lst.append(v)
    else:
        verti_lst.append(v)
hori_lst = hori_lst + [verti_total]
verti_lst = verti_lst + [hori_total]
print("hori_lst:",hori_lst)
print("veti_lst:",verti_lst)

def get_lst(lst_item):
    array = []
    start = 0
    for i in range(len(lst_item)):
        lst = []
        for item in range(start, lst_item[i]):
            lst.append(item)
        start = lst_item[i]
        array.append(len(lst))
    return array

print("hori_array:", get_lst(hori_lst))
print("verti_array:", get_lst(verti_lst))

print(max(get_lst(hori_lst))*max(get_lst(verti_lst)))