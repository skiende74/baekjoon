N, T = map(int,input().split())
tp = list(sorted([list(map(int,input().split())) for _ in range(N)]))
dp = [10**9]*(T+1)
dp[0] = sum(map(lambda x: x[1], tp))
for time, penalty in tp:
    for i in range(time, T+1)[::-1]:
        dp[i] = min(dp[i], dp[i-time]-penalty)
print(min(dp))