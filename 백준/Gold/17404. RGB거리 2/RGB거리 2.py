import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

ans = 10**9

for l in range(3):
    dp = [[10**9]*3 for _ in range(N)]
    dp[0][l] = grid[0][l]    
    for i in range(1, N):
        dp[i][0] = grid[i][0] + min(dp[i-1][2], dp[i-1][1]) 
        dp[i][1] = grid[i][1] + min(dp[i-1][0], dp[i-1][2]) 
        dp[i][2] = grid[i][2] + min(dp[i-1][1], dp[i-1][0]) 
    
    for j in range(3):
        if l == j: continue
        ans = min(ans, dp[-1][j])
print(ans)