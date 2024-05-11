import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

dp = [[[10**9]*3 for _ in range(N)] for _ in range(3)]
dp[0][0][0] = grid[0][0]
dp[1][0][1] = grid[0][1]
dp[2][0][2] = grid[0][2]

for k in range(3):
    for i in range(1, N-1):
        for j in range(3):
            for j0 in range(3):
                if j==j0: continue
                dp[k][i][j] = min(dp[k][i][j], dp[k][i-1][j0] + grid[i][j])

ans = 10**9
for k in range(3):
    for i in range(3):
        for j in range(3):
            if k == i or k==j: continue
            ans = min(ans, dp[i][N-2][j] + grid[N-1][k])
print(ans)