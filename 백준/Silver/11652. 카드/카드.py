from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
Counter = defaultdict(lambda: 0)
max_val = 0
max_idx = []
for _ in range(N):
    num = int(input())
    Counter[num] += 1
    if max_val < Counter[num]:
        max_val = Counter[num]
        max_idx = [num]
    elif max_val == Counter[num]:
        max_idx.append(num)
print(min(max_idx))