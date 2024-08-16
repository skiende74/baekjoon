import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    coins = [0]+list(map(int,input().split()))
    M = int(input())

    dp = [[0]*(M+1) for _ in range(N+1)] # dp[동전수][돈]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(M+1):
            for k in range(j//coins[i]+1):
                dp[i][j] += dp[i-1][j-k*coins[i]]
    print(dp[N][M])