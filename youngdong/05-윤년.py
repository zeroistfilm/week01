# https://www.acmicpc.net/problem/2753

year = int(input())


if year%4==0:
    if year%100!=0:
        leapyear = 1
        if year%400==0:
            leapyear =1
    else:
        if year%400!=0:
            leapyear =0
        else:
            leapyear=1

else:
    leapyear=0
print(leapyear)