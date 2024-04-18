N = int(input())
seq = list(map(int,input().split()))
dp = [1]*(N)
dp[0]=1
for i in range(N):
    for j in range(i):
        if seq[j]<seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

result = []
x = max(dp)
for i in range(N-1, -1,-1):
    if dp[i] == x:
        result.append(seq[i])
        x -= 1
print(*result[::-1])