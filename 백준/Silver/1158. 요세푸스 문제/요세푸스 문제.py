N, K = map(int, input().split())
nums = list(range(1, N+1))

i = 0
result = []
for _ in range(N):
    i = (i+K-1)%len(nums)
    num = nums.pop(i)
    result.append(str(num))

print('<' + ', '.join(result) + '>')