import sys
N, M, K = map(int,input().split())
input = lambda: sys.stdin.readline().rstrip()
grid = [['X']*(M+1)]+[ ['X']+list(input()) for _ in range(N)]

prefix_sum = [[ [0]*(M+1) for _ in range(N+1)] for _ in range(2)]

for i in range(1,N+1):
    for j in range(1, M+1):
        prefix_sum[0][i][j] = prefix_sum[0][i][j-1] + prefix_sum[0][i-1][j] - prefix_sum[0][i-1][j-1] + (grid[i][j]!='BW'[(i+j)%2])
        prefix_sum[1][i][j] = prefix_sum[1][i][j-1] + prefix_sum[1][i-1][j] - prefix_sum[1][i-1][j-1] + (grid[i][j]!='BW'[(i+j+1)%2])
def find(k, i, j): return prefix_sum[k][i][j] - prefix_sum[k][i-K][j] - prefix_sum[k][i][j-K] + prefix_sum[k][i-K][j-K]
ans = 10**9
for i in range(K, N+1):
    for j in range(K, M+1):
        ans = min(ans, find(0,i,j),find(1,i,j))
print(ans)