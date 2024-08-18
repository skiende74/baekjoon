N, K = map(int, input().split())
W = [0]
P = [0]


for _ in range(N):
    w, p = map(int, input().split())
    W.append(w)
    P.append(p)

dp = [[0]*(K+1), *[[0, *[-1]*K] for _ in range(N)]]

def knapsack(i, w):
    if dp[i][w] != -1:
        return dp[i][w]
    if w < W[i]:
        dp[i][w] = knapsack(i-1, w)
    else:
        dp[i][w] = max(knapsack(i-1,w), knapsack(i-1, w-W[i])+P[i])
    return dp[i][w]

print(knapsack(N, K))