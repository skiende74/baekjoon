N = int(input())

MAX = 10**9
dp=[MAX]*(10**6+1)
dp[0] = 0
dp[1] = 0
for i in range(1, min(N+1,10**6+1)):
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i >= 1:
        dp[i] = min(dp[i], dp[i-1]+1)
print(dp[N])