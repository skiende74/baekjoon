import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
dp = [[0]*(K+1) for _ in range(M+1)]

for _ in range(N):
    m, k = map(int,input().split())
    for i in range(m, M+1)[::-1]:
        for j in range(k, K+1)[::-1]:
            dp[i][j] = max(dp[i][j], dp[i-m][j-k]+1)
print(max(map(max,dp)))