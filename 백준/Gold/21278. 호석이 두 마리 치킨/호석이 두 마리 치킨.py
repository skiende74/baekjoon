import sys
input = sys.stdin.readline
V, E = map(int,input().split())
INF = 10**9
grid = [[INF]*(V+1) for _ in range(V+1)]
for i in range(1,V+1): grid[i][i] = 0
for _ in range(E):
    i,j = map(int,input().split())
    grid[i][j] = 1
    grid[j][i] = 1

for k in range(1,V+1):
    for i in range(1,V+1):      
        for j in range(1,V+1):
            grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])

min_dist = 2*INF
for s1 in range(1,V+1):
    for s2 in range(s1+1, V+1):
        dist = sum([min(grid[s1][e], grid[s2][e]) for e in range(1,V+1)])
        min_dist = min(min_dist, dist)

answers = []
for s1 in range(1,V+1):
    for s2 in range(s1+1, V+1):
        dist = sum([min(grid[s1][e], grid[s2][e]) for e in range(1,V+1)])
        if dist == min_dist:
            answers.append([s1,s2])
print(*sorted(answers)[0], min_dist*2)