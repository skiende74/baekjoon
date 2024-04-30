q = int(input())

dp=[0]*(10**6+1)
dp[1] = 1
for i in range(2, 10**6+1):
    dp[i] = abs(dp[i-1] + dp[i-2])%10**9

if q<0 and -q%2==0:
    print(-1)
elif q==0:
    print(0)
else:
    print(1)

print(dp[abs(q)])