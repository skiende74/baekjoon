N, K = map(int,input().split())
dp = [0]*(N+1)
dp[0] = 1

goods = [i for i in range(1, N+1)
    if i % sum(map(int, str(i))) ==0]

for good in goods:
    for i in range(good, N+1):
        dp[i] = (dp[i]+dp[i-good]) % K
print(dp[N])