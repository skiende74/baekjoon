from collections import deque
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

me = (-1,-1)
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            me = (i,j)
            grid[i][j] = 0

def bfs(i,j):
    global eaten, inner_cnt, i2, j2

    goal = 10**9
    Q = deque([((i,j),0)])
    visited = set([(i,j)])
    candi = []
    while Q:
        (i, j), inner_cnt = Q.popleft()
        for di,dj in zip([-1,0,0,1],[0,-1,1,0]):
            i2,j2 = i+di, j+dj
            if not (0<=i2<N and 0<=j2<N): continue
            if (i2,j2) in visited: continue
            if grid[i2][j2] > mine: continue
            if inner_cnt >= goal: continue
            visited.add((i2,j2))
            Q.append(((i2,j2), inner_cnt+1))
            if grid[i2][j2] < mine and grid[i2][j2] > 0: 
                goal = inner_cnt+1
                candi.append((i2,j2))
    if candi:
        i2,j2 = sorted(candi)[0]
        grid[i2][j2] = 0
        eaten += 1
        inner_cnt = goal

eaten = 0
mine = 2
total_cnt = 0
i2,j2 = me
while True:
    inner_cnt = 0
    eaten_old = eaten
    bfs(i2, j2)
    if eaten_old == eaten: break

    total_cnt += inner_cnt
    if eaten == mine:
        eaten = 0
        mine += 1
print(total_cnt)    