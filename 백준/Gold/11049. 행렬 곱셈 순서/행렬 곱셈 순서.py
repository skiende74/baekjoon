import sys
n = int(input())
INF = 2**31
rcs = [ [INF,INF]]
for _ in range(n):
    rcs.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][i] = 0

for l in range(1,n):
    for i in range(1,n+1-l):
        j = i+l
        for k in range(i+1,j+1):
            dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k][j] + rcs[i][0]*rcs[k][0]*rcs[j][1])
print(dp[1][n])