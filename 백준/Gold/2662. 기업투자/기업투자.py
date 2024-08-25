N, M = map(int,input().split()) # 투자금, 기업수
dp = [0 for _ in range(N+1)]
mem = [{} for _ in range(N+1)]

prices = [[0] for _ in range(M+1)]
for i in range(1, N+1):
    _, *p = map(int,input().split())
    for j in range(1, M+1): prices[j].append(p[j-1])

for k in range(1, M+1): # 여러 종류의 기업
    dp0 = dp.copy()
    for i in range(N+1)[::-1]: # 현재dp 고려 금액 
        for j in range(i+1): # 이번에 넣는금액
            if dp0[i-j]+prices[k][j] > dp[i]:
                dp[i] =  dp0[i-j]+prices[k][j] # 가치
                mem[i] = mem[i-j].copy()
                mem[i][k] = j
                # mem[i-j]
print(dp[-1])
#print(mem)
ans = [0]*(M+1)
for k, v in sorted(mem[-1].items()):
    ans[k] = v
print(*ans[1:])