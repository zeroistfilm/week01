import sys

def get_prime():
    a = [False,False,True] + [True, False] * 5000
    for number in range(3, 101, 2):
        if a[number]:
            a[number * 2::number] = [False] * len(a[number * 2::number])
    return a


for i in range(int(sys.stdin.readline())):
    item = int(sys.stdin.readline())
    if item == 4:
        print(2, 2)
        continue
    half_item = item // 2
    if half_item % 2 == 0:
        half_item += 1
    for i in range(half_item, -1, -2):
        if get_prime()[i] and get_prime()[item - i]:
                if i > item - i:
                    print (item - i, i)
                    break
                print (i, item - i)
                break

