import sys

def get_prime(n):
    hansu_list_default = [False] + [True]*99 + [False]*901
    hansu_list=[]
    if n < 100:
        return n
    for i in range(100,n+1):
        exp = list(map(int, str(i)))
        if hansu_list_default[i] == True:
            continue
        if exp[2] - exp[1] == exp[1] - exp[0]:
            hansu_list_default[i] = True
            hansu_list.append(i)
            # 한번 한수를 찾으면 거꾸로 나오는 수도 한수인데 그것도 같이 처리하는게 좋을지, 아니면 자기 차례가 올때 한수 판별을 하는게 나을지
            # reverse_num = exp[2]*100 + exp[1]*10 + exp[0]
            # if revere_num not in hansu_list:
            #     hansu_list_default[reverse_num] = True
            #     hansu_list.append(reverse_num)
    print("hansu_list:",hansu_list)
    result = 99 + len(hansu_list)
    print("result:",result)
    return result

print(get_prime(int(sys.stdin.readline())))