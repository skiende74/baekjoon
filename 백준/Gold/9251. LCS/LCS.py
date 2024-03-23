A = list(input())
B = list(input())

N1 = len(A)
N2 = len(B)
dp = [[0 for _ in range(N2)] for  _ in range(N1) ]
dp[0][0] = 1 if A[0]==B[0] else 0

for j in range(1, N2):
    dp[0][j] = max(dp[0][j-1], 1 if A[0] == B[j] else 0)
for i in range(1, N1):
    dp[i][0] = max(dp[i-1][0], 1 if A[i] == B[0] else 0)
for i in range(1, N1):
    for j in range(1, N2):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])