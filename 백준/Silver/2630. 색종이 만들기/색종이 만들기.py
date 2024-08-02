def dnc(i,j,sz):
    if sz == 0: 
        ans[grid[i][j]] += 1
        return
    
    s = {grid[i2][j2]
         for i2 in range(i, i+2**sz)
         for j2 in range(j, j+2**sz)}
    if len(s) == 1:
        ans[grid[i][j]] += 1
        return
    
    sz -= 1
    dnc(i, j, sz)
    dnc(i, j+2**sz, sz)
    dnc(i+2**sz, j, sz)
    dnc(i+2**sz, j+2**sz, sz)
    

from math import log2

N = int(input())
n = int(log2(N))

grid = [list(map(int,input().split())) for _ in range(N)]
ans = [0, 0]

dnc(0,0,n)
print(' '.join(map(str, ans)))