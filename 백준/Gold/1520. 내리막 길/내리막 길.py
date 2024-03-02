import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*(N) for _ in range(M)]
dp[0][0] = 1

def route(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    result = 0
    for di, dj in zip([-1,1,0,0],[0,0,-1,1]):
        if 0 <= i+di < M and 0 <= j+dj < N and A[i][j] < A[i+di][j+dj]:
            result += route(i+di,j+dj)
    dp[i][j] = result
    return dp[i][j]

print(route(M-1,N-1))