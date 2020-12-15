import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
def hanoi_path(plate: int, start:int, end: int) -> None:
    middle = 6-start-end
    if plate < 1:
        return
    if plate <= 20:
        # 이 부분도 사실 원리 상 start -> end로 가면 되는거다. middle을 새로운 end로 생각하고 움직이는 함수라고 생각할 수 있음.
        hanoi_path(plate-1,start,middle)
    # 이 부분은 한번만 최종적으로 움직이면 됨.
        print(f"{start} {end}")
        # 이 부분도 사실 원리 상 start -> end이다. middle을 새로운 start로 생각하고 움직이면 됨. 기존의 start가 middle이 되면 됨.
        # print(f" 3번째 구절 : {plate-1}를 {middle}에서 {end}로 이동")
        hanoi_path(plate-1,middle,end)

def hanoi_num(plate):
    return 2**(plate)-1

print(hanoi_num(n))
hanoi_path(n,1,3)


