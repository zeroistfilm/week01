range_num = int(input())

for i in range(range_num):
    org_list = list(map(int, input().split()))
    avg = sum(org_list[1:]) / org_list[0]
    new_list = [item for item in org_list[1:] if item > avg]
    print(f'{format(len(new_list)/len(org_list[1:]) *100.0, ".3f")}%')