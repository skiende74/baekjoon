import sys
input = sys.stdin.readline

V, Q = map(int,input().split())
grid = [0]+[[0]+list(map(int, input().split())) for _ in range(V)]

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])

for _ in range(Q):
    i,j,T = map(int,input().split())
    print("Enjoy other party" if grid[i][j]<=T else "Stay here")