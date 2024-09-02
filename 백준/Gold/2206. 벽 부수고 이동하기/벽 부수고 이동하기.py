from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
grid = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1

def bfs():
    Q = deque([(0,0,0)])
    while Q:
        i,j,a = Q.popleft()
        if (i,j) == (N-1,M-1):
            return visited[i][j][a]
        dis, djs = [0,0,-1,1],[-1,1,0,0]
        for di, dj in zip(dis,djs):
            i2, j2 = i+di, j+dj
            if not(0<=i2<N and 0<=j2<M): continue
            if grid[i2][j2] == 1 and a==0:
                visited[i2][j2][1] = visited[i][j][0] + 1
                Q.append((i2,j2, 1))
            if grid[i2][j2]==0 and visited[i2][j2][a]==0:
                visited[i2][j2][a] = visited[i][j][a] + 1
                Q.append((i2,j2, a))
            
    return -1

print(bfs())