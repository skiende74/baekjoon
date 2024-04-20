import sys
input = sys.stdin.readline
N, T = map(int,input().split())
T=T+1
seq = [int(input()) for _ in range(N)]
dp = [[0]*T for _ in range(N)]
for t in range(T):
    dp[0][t] = 1 if seq[0] == (1+(t%2==1)) else 0
for i in range(1, N):
    for t in range(T):
        dp[i][t] = max(dp[i-1][max(0, t-1):t+1]) + (1 if seq[i] == (1+(t%2==1)) else 0)
print(max(dp[-1]))