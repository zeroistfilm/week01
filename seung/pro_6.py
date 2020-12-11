x,y,w,h = map(int,input().split())
print(f'{x},{y},{w},{h}')
print(type(x))

if x > w/2:	result1 = w-x
elif x <= w/2: result1 = x - 0

if y > h/2 : result2 = h-y
elif y <= h/2 : result2 = y-0

print(min(result1,result2))