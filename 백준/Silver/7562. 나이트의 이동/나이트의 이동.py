from collections import deque

def solve():
    N = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int,input().split()))

    MAX = 10**9
    dist = [[MAX]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    def bfs(start):
        Q = deque([start])
        dist[start[0]][start[1]] = 0
        visited[start[0]][start[1]] = True
        while Q:
            i,j = Q.popleft()
            dis = [-2, -2, -1, -1,  1, 1,  2, 2]
            djs = [-1,  1, -2,  2, -2, 2, -1, 1]
            for di,dj in zip(dis, djs):
                i2, j2 = i+di, j+dj
                if 0<=i2<N and 0<=j2<N and not visited[i2][j2]:
                    visited[i2][j2] = True
                    dist[i2][j2] = dist[i][j] + 1
                    Q.append((i2, j2))
                    if (i2,j2) == end:
                        return dist[i2][j2]
        return 0
    print(bfs(start))

for _ in range(int(input())):
    solve()