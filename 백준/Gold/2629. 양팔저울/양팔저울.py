def dfs(i, w):
    if i>N or dp[i][w]: return

    dp[i][w] = True
    dfs(i+1, w)
    dfs(i+1, w+weight[i])
    dfs(i+1, abs(w-weight[i]))

N = int(input())
weight = list(map(int,input().split())) +[0]
M = int(input())
balls = list(map(int,input().split()))

dp = [[False]*15001 for _ in range(N+1)]
dfs(0, 0)
for b in balls:
    print('Y' if b<=15000 and dp[N][b] else 'N', end =' ')