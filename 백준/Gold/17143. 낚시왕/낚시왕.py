def next_pose(s, d, i, j):
    if d == 1:
        if i-s<0: return next_pose((s-i)%(2*N-2), 2, 0, j)
        return (i-s, j, d)
    if d == 2:
        if i+s>N-1: return next_pose((s-(N-1-i))%(2*N-2), 1, N-1, j)
        return (i+s, j, d)
    if d == 3:
        if j+s>M-1: return next_pose((s-(M-1-j))%(2*M-2), 4, i, M-1)
        return (i, j+s, d)
    else:
        if j-s<0: return next_pose((s-j)%(2*M-2), 3, i, 0)
        return (i, j-s, d)

def move_shark():
    deletes, adds = [], []
    for i in range(N):
        for j in range(M):
            if not grid[i][j]: continue
            deletes.append((i,j))
            s,d,z = grid[i][j]
            i2, j2, d2 = next_pose(s,d,i,j)
            adds.append((i2, j2, (s,d2,z)))
    for i,j in deletes: grid[i][j] = 0
    for i2, j2, shark in adds:
        if grid[i2][j2] and grid[i2][j2][2] > shark[2]: continue
        grid[i2][j2] = shark

def fishing():
    global ans
    for i in range(N):
        if grid[i][j]:
            s,d,z = grid[i][j]
            grid[i][j] = 0
            ans += z
            return

import sys
sys.setrecursionlimit(10**4)
input = lambda: sys.stdin.readline().rstrip()
N, M, S = map(int,input().split())
grid = [[0]*M for _ in range(N)]
for _ in range(S):
    i, j , s, d, sz = map(int,input().split())
    grid[i-1][j-1] = (s,d,sz)

ans = 0
for j in range(M):
    fishing()
    move_shark()
print(ans)