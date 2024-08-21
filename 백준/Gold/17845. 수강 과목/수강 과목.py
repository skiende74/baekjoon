import sys
input = sys.stdin.readline
T, K = map(int,input().split())
dp = [0]*(T+1)
for _ in range(K):
    score, time = map(int,input().split())
    for i in range(time, T+1)[::-1]:
        dp[i] = max(dp[i], dp[i-time]+score)
print(max(dp))