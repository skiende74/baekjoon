import sys
input = sys.stdin.readline
L, P = map(int,input().split())
dp = [0]*(L+1)
dp[0] = 10**9
for _ in range(P):
    l, c = map(int,input().split())
    for i in range(l, L+1)[::-1]:
        dp[i] = max(dp[i], min(dp[i-l], c))
print(dp[L])