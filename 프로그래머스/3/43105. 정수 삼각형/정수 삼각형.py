def solution(triangle):
    N = len(triangle)
    dp = [[0]*N for _ in range(N)]
    
    for i in range(N): dp[i][0] = triangle[i][0]
    for i in range(1, N):
        for j in range(i+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    return max(dp[-1])