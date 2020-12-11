a = int(input())

print(a in range(90,101))

if a in range(90,101):
    print("A")
elif a in range(80,90):
    print("B")
elif a in range(70,80):
    print("C")
elif a in range(60,70):
    print("D")
else:
    print("F")