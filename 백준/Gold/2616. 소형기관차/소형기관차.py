import sys
input = sys.stdin.readline
from itertools import accumulate
N = int(input())
seq = [0] + list(map(int,input().split()))
K = int(input())

prefix_sum = list(accumulate(seq))
def range_sum(i): return prefix_sum[i]-prefix_sum[i-K]
dp = [[0]*(N+1) for _ in range(3)]

for i in range(K, N+1): dp[0][i] = max(dp[0][i-1], range_sum(i))

for i in range(2*K, N+1):
    dp[1][i] = max(dp[1][i-1], dp[0][i-K] + range_sum(i))
for i in range(3*K, N+1):
    dp[2][i] = max(dp[2][i-1], dp[1][i-K] + range_sum(i))
print(dp[-1][-1])
