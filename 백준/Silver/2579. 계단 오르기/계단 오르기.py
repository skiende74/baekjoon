import sys
input = sys.stdin.readline
N = int(input())

MIN = -10**8
seq = [0] + [int(input()) for _ in range(N)]
dp = [[MIN,MIN] for _ in range(N+1)]
dp[0] = [0, 0]
dp[1] = [seq[1], MIN]
for i in range(2,N+1):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + seq[i]
    dp[i][1] = dp[i-1][0] + seq[i]
print(max(dp[-1]))