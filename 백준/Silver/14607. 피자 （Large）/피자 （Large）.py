def dfs(i):
    if i in dp: return dp[i]
    dp[i] = i//2 * (i-i//2) + dfs(i//2)+dfs(i-i//2)
    return dp[i]
n = int(input())
dp = {1:0}
print(dfs(n))