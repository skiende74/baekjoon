N, k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def mat_mult(A,B):
    N
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += (A[i][k] * B[k][j]) % 1000
    return res

def dfs(k):
    if k == 1: return A
    if k % 2 == 0: 
        half = dfs(k//2)
        return mat_mult(half, half)
    return mat_mult(A, dfs(k-1))

result = dfs(k)

for i in range(N):
    for j in range(N):
        print(result[i][j]%1000, end=' ')
    print()