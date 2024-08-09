def dfs(i,j,n):
    res = [0]*3
    if n==1:
        res[grid[i][j]] += 1
        return res
    for di in range(3):
        for dj in range(3):
            i2, j2 = i + n*di//3, j + n*dj//3
            r = dfs(i2, j2, n//3)
            res[0] += r[0]
            res[1] += r[1]
            res[2] += r[2]
    if res == [9,0,0] or res == [0,9,0] or res == [0,0,9]:
        res = list(map(lambda x: x//9, res))
    return res

import sys
input = sys.stdin.readline
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
ans = dfs(0,0,N)
print('\n'.join(map(str, [ans[-1],ans[0],ans[1]])))