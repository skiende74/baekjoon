N = int(input())
right = list(map(int,input().split()))
up = []
up.append(list(map(int,input().split())))
up.append(list(map(int,input().split())))

dp = [[0,0,0] for _ in range(N)]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + up[0][i-1]
dp[0][1] = right[0]
dp[0][2] = 0

for i in range(1,N):
    cross = dp[i][0] + right[i]
    go_up = dp[i-1][1]+up[1][i-1]

    if cross < go_up:
        dp[i][1] = cross
        dp[i][2] = i
    else:
        dp[i][1] = go_up
        dp[i][2] = dp[i-1][2]
print(dp[-1][2]+1,dp[-1][1])