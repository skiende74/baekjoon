N, T = map(int,input().split())
dp = [0]*(T+1)
for time, score in [ map(int,input().split()) for _ in range(N)]:
    for i in range(time, T+1)[::-1]:
        dp[i] = max(dp[i], dp[i-time]+score)
print(max(dp))