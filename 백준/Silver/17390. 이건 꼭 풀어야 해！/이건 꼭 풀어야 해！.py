from itertools import accumulate
import sys
input = sys.stdin.readline

N, Q = map(int,input().split())
seq = [0] + list(sorted(map(int,input().split())))
p_sum = list(accumulate(seq))
for _ in range(Q):
    i, j = map(int,input().split())
    print(p_sum[j] - p_sum[i-1])
