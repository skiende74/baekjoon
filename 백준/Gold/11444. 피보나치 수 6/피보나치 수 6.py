def mat_mul(A,B): 
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(len(B[0])):
            for k in range(2):
                res[i][j] += A[i][k]*B[k][j]
            res[i][j] %= 1_000_000_007
    return res

A = [[1,1],[1,0]]
def dfs(i):
    if i == 1: return A
    if i % 2 == 0:
        half = dfs(i//2)
        return mat_mul(half, half)
    return mat_mul(A, dfs(i-1))

R = dfs(int(input()))
print(R[1][0])