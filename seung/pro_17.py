num = int(input())

for i in range(num):
    recipe = input().split()
    ans = ''
    for item in recipe[1]:
        ans += item*int(recipe[0])
    print(ans)