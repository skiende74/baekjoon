import sys
input = sys.stdin.readline
N, M, H = map(int,input().split())
dp = [0]*(H+1)
dp[0] = 1
for _ in range(N):
    blocks = list(map(int, input().split()))
    blocks.sort()
    dp2 = [0]*(H+1)
    for b in blocks:
        for i in range(b, H+1)[::-1]:
            dp2[i] = (dp2[i] + dp[i-b]) % 10007
    for i in range(H+1):
        dp[i] = (dp[i] + dp2[i]) % 10007
print(dp[H])