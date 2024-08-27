def solution(x, y, n):
    dp = [1e9]*(y+1)
    dp[x]=0
    for i in range(x+1, y+1):
        if i%2 == 0: dp[i] = min(dp[i], dp[i//2]+1)
        if i%3 == 0: dp[i] = min(dp[i], dp[i//3]+1)
        dp[i] = min(dp[i], dp[i-n]+1)
    return dp[y] if dp[y] != 1e9 else -1