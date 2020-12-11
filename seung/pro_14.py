from collections import Counter,OrderedDict

ans = 150*266*427

counter = Counter((str(ans)))
print(counter)

for i in range(10):
    if str(i) not in counter:
        counter[str(i)] = 0
ordered_dict = OrderedDict(sorted(counter.items(),key=lambda  t:t[0]))
print("ans:",ordered_dict.values())

for v in ordered_dict.values():
    print(v)