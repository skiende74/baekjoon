import sys
input = sys.stdin.readline

N = int(input())
seq = [list(map(int, input().split())) for _ in range(N)]

nums = []
for s,e in seq:
    nums.append((s,1))
    nums.append((e,-1))
nums.sort()
count = 0
max_count = 0
for _, c in nums:
    count += c
    max_count = max(max_count, count)

print(max_count)