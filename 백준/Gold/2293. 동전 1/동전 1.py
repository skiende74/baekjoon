N, K = map(int, input().split())
seq = [int(input()) for _ in range(N)]
seq = list(set(seq))
seq.sort()

dp = [0]*(K+1)
dp[0] = 1

for s in seq:
    for i in range(1, K+1):
        if i-s>=0:
            dp[i] += dp[i-s]

print(dp[K])