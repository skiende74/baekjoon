import sys
input = sys.stdin.readline
N, M, Q = map(int,input().split())
grid = [[0]*(M+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]
p_sum = [[0]*(M+1) for _ in range(N+1)] 

for i in range(1, N+1):
    for j in range(1, M+1):
        p_sum[i][j] = p_sum[i-1][j] + p_sum[i][j-1] - p_sum[i-1][j-1] + grid[i][j]
for _ in range(Q):
    i1,j1,i2,j2 = map(int,input().split())
    print( (p_sum[i2][j2] - p_sum[i2][j1-1] - p_sum[i1-1][j2] + p_sum[i1-1][j1-1])//((i2-i1+1)*(j2-j1+1)) )