import sys
input = sys.stdin.readline
V, E = map(int,input().split())
INF = 10**9
grid = [[INF]*(V+1) for _ in range(V+1)]
for i in range(1,V+1): grid[i][i] = 0
for _ in range(E):
    i,j,w = map(int,input().split())
    grid[i][j] = w

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

Q = int(input())
queries=list(map(int,input().split()))

Xs = [INF]+[max([grid[i][q]+grid[q][i] for q in queries]) for i in range(1,V+1)]
min_Xs = min(Xs)
answers=[i for i in range(1,V+1)
    if Xs[i] == min_Xs]
print(*answers)