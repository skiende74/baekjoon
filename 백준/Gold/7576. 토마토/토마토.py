from collections import deque

M, N = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

def bfs(start):
    Q = deque(starts)
    inner_count = len(Q)
    count = 0
    while Q:
        i, j, count = Q.popleft()
        dis, djs = [0,0,-1,1],[-1,1,0,0]
        for di, dj in zip(dis,djs):
            i2, j2 = i+di, j+dj
            if 0<=i2<N and 0<=j2<M and grid[i2][j2] == 0:
                grid[i2][j2] = 1
                inner_count += 1
                Q.append((i2,j2, count+1))
    return count, inner_count

starts = [(i,j,0) for i in range(N) for j in range(M) if grid[i][j] == 1]
count = bfs(starts)
has_zero = any((i,j,0) for i in range(N) for j in range(M) if grid[i][j] == 0)

print(count[0] if not has_zero else -1)