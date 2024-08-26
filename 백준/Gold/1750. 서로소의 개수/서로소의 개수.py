from math import gcd
import sys
input = sys.stdin.readline
N = int(input())
seq = [int(input()) for _ in range(N)]
seq.sort()

dp = [0]*(100_000+1)
for s in seq:
    dp[s] = (2*dp[s]+1) % 10_000_003
    for i in range(1, s):
        dp[gcd(i,s)] = (dp[gcd(i,s)]+dp[i]) % 10_000_003
print(dp[1])