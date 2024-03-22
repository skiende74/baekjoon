import sys
input = sys.stdin.readline

N = int(input())
seq = [int(input()) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
dp[0] = [0, seq[0],seq[0]]
for i in range(1,N):
    dp[i][2] = dp[i-1][1] + seq[i]
    dp[i][1] = dp[i-1][0] + seq[i]
    dp[i][0] = max(dp[i-1])

print(max(dp[-1]))