num = int(input())
#
# def get_factorial(n: int)-> int:
#     if n > 0:
#         return  n * get_factorial(n-1)
#     else:
#         return 1
#
# print(get_factorial(num))

if num == 1:
	print(1)
else :
	fac = 1
	for i in range(1,num+1):
		fac = fac*i
	print(fac)