from math import ceil

N, M, K = map(int,input().split())
damages = [int(input()) for _ in range(N)]
damages.sort()
bosses = [list(map(int, input().split())) for _ in range(K)]

T = 15*60


damages = damages[len(damages)-M:]

ans = 0
for damage in damages:
    dp = [0] * (T+1)
    for hp, money in bosses:
        for i in range(ceil(hp/damage), T+1)[::-1]:
            dp[i] = max(dp[i], dp[i-ceil(hp/damage)] + money)
    ans += max(dp)
print(ans)