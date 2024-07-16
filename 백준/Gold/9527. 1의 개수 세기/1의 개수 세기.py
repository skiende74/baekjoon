from itertools import accumulate

A, B = map(int,input().split())

def f(x):
    if x > 255: return f(x // 256) + f(x % 256)
    return dp[x]

def cf(x):
    if x > 255: return ((x // 256))*cf(255) + cf((x // 256)-1) * 256 + cf(x % 256) + (x%256 +1)*f(x//256)
    return prefix_sum[x]

dp = [0]*256
dp[1] = 1
dp[2] = 1

for i in range(1, 255+1): dp[i] = dp[i//2] + i%2
prefix_sum = list(accumulate(dp))

print(cf(B)-cf(A-1))