N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums0 = list(map(lambda x: x%K, nums))

dp = [[0]*K  for _ in range(M+1)] # dp[n][m][k]

for m in range(M):
    for n in range(N):
        for k in range(K):
            x = dp[m][k] + nums[n]
            dp[m + 1][x % K] = max(x, dp[m+1][x % K])
print(dp[M][0])