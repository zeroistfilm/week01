# 솔루션1
def solve(a:list) -> int:
	sum = 0
	for item in a:
		sum += item
	return sum

# 솔루션2(28ms)
def solve(a:list) -> int:
	ans = sum(a)
	return ans