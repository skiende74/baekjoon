import sys
input = sys.stdin.readline

N = int(input())
seq = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N+3)]
dp[0] = seq[0]
for i in range(1,N):
    dp[i] = max(dp[i-3]+seq[i-1]+seq[i], dp[i-2]+seq[i])
    dp[i] = max(dp[i], dp[i-1])
print(dp[N-1])