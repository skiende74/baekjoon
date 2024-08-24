N, M = map(int,input().split())
seq = list(map(int,input().split()))
values = list(map(int,input().split()))
seq = [(seq[i],values[i]) for i in range(N)]
seq.sort(key=lambda x:(x[1],x[0]))
dp = [0]*(10001)
for s,val in seq:
    for i in range(val,10000+1)[::-1]:
        dp[i] = max(dp[i],dp[i-val]+s)
for i in range(10000+1):
    if dp[i] >=M:
        print(i)
        break
else: print(-1)