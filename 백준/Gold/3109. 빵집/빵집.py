import sys
input = lambda: sys.stdin.readline().rstrip()
def dfs(i,j):
    global success, ans
    if j == M-1:
        success = True
        ans += 1
        return
    for di,dj in zip([-1,0,1],[1,1,1]):
        if success: continue
        i2,j2 = i+di, j+dj
        if not (0<=i2<N and 0<=j2<M): continue
        if visited[i2][j2]: continue
        if grid[i2][j2]=='x': continue
        visited[i2][j2] = True
        dfs(i2, j2)
        # if not success: visited[i2][j2] = False

N, M = map(int,input().split())
grid = [input() for _ in range(N)]

ans = 0
visited = [[False]*M for _ in range(N)]
for i in range(N):
    success = False
    dfs(i, 0)
# for v in visited:
#     print(*v, sep =' ')
print(ans)