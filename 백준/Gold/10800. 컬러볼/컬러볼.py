from itertools import accumulate
from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
nums_c = [ [0] for _ in range(N+1)]
nums = [0]
seq = []
for _ in range(N):
    c, n = map(int, input().split())
    seq.append([c,n])
    nums_c[c].append(n)
    nums.append(n)
nums.sort()
for i in range(N+1): nums_c[i].sort()

prefix_sum = list(accumulate(nums))
prefix_sum_c = [list(accumulate(nums_c[i])) for i in range(N+1)]

def get(c, n):
    res = prefix_sum[bisect_left(nums, n)-1]
    return res - prefix_sum_c[c][bisect_left(nums_c[c], n)-1] 
for c,n in seq: print(get(c,n))
