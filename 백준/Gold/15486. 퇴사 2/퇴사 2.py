import sys
input = sys.stdin.readline
N = int(input())
seq = [list(map(int,input().split())) for _ in range(N)]
seq_rev = seq[::-1]
dp = [0]*(N)
for i in range(N):
    now = seq_rev[i][1]+dp[i-seq_rev[i][0]] if i-seq_rev[i][0]>=-1 else 0
    dp[i] = max(now, dp[i-1])
print(dp[-1])