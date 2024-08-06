def grid_sum(i,j,k):
    return sum([ grid[a][b] 
      for a in range(i, i+k)
        for b in range(j, j+k)
        ])

def dfs(i, j, k):
    K = 2 ** k
    
    G = grid_sum(i, j, K)
    if G == K**2 or G == 0:
        print(1 if G == K**2 else 0, end='')
        return

    print('(', end='')
    dfs(i, j, k-1)
    dfs(i, j+K//2, k-1)
    dfs(i+K//2, j, k-1)
    dfs(i+K//2, j+K//2, k-1)
    print(')', end='')

from math import log2

N = int(input())
grid = [ list(map(int, input())) for _ in range(N) ]

k = int(log2(N))

dfs(0,0,k)