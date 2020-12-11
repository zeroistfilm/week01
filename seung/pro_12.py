range_num = int(input())

for i in range(range_num):
	inp = list(input())
	print(get_score(inp))

def get_score(inp):
	count = 0
	sum = 0
	for i,value in enumerate(inp):
		if value = "O":
			count +=1
			sum += count
		else:
			count = 0
	return sum