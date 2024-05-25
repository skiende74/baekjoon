N = int(input())
seq = list(map(int, input().split()))
quota = int(input())

left = 0
right = max(seq)
while left <= right:
	mid = (left + right) // 2
	total = 0
	for budget in seq:
		total += min(budget, mid)
	if total == quota:
		break
	elif total > quota:
		right = mid-1
	else:
		left = mid + 1
total = 0
for budget in seq:
		total += min(budget, mid)
if total>quota:
	mid -= 1
print(mid)