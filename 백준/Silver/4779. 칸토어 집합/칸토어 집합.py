def recursive(N):
    if dp[N] != '': return dp[N]
    dp[N] = recursive(N-1) + ' '*(3**(N-1)) + recursive(N-1)
    return dp[N]
    
dp = ['']*14
dp[0] = '-'
import sys
lines = list(map(int, sys.stdin.read().split()))
for n in lines:
    print(recursive(n))
    