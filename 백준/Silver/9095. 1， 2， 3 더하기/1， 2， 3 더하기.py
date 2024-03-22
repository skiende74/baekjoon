dp = [0]*(20)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(3, 20):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
T = int(input())
for _ in range(T):
    print(dp[int(input())])