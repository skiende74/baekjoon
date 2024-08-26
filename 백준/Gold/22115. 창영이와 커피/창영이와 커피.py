N, C = map(int,input().split())
dp = [10**9]*(C+1)
dp[0] = 0
for c in list(sorted(map(int,input().split()))):
    for i in range(c, C+1)[::-1]:
        dp[i] = min(dp[i], dp[i-c]+1)
print(dp[C] if dp[C] != 10**9 else -1)