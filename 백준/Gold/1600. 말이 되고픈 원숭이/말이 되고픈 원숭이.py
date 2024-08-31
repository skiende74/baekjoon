from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
M, N = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
visited[0][0] = [True]*(K+1)
def bfs(start):
    Q = deque(start)
    while Q:
        i, j, k, d = Q.popleft()
        if (i,j) == (N-1,M-1): return d
        for di, dj in zip([0,0,-1,1],[-1,1,0,0]):
            i2, j2 = i+di, j+dj
            if not (0<=i2<N and 0<=j2<M) or visited[i2][j2][k]: continue
            if grid[i2][j2] == 1: continue
            visited[i2][j2][k] = True
            Q.append((i2,j2,k,d+1))
        if k >= 1:
            for di, dj in zip([-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]):
                i2, j2 = i+di, j+dj
                if not (0<=i2<N and 0<=j2<M) or visited[i2][j2][k-1]: continue
                if grid[i2][j2] == 1: continue
                visited[i2][j2][k-1] = True
                Q.append((i2,j2,k-1,d+1))
    return -1
print(bfs([(0,0,K,0)]))