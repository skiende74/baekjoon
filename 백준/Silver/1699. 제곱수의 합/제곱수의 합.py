N = int(input())
dp = [10**9]*(N+1)
dp[0]=0
dp[1]=1
for i in range(2, N+1):
    for j in range(1, int(N**0.5)+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)
print(dp[N])