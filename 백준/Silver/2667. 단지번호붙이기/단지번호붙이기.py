N = int(input())
grid = [list(map(int, list(input()) )) for _ in range(N)]

visited=[[False]*N for _ in range(N)]

def dfs(i,j):
    global count
    dis,djs=[0,0,-1,1], [-1,1,0,0]
    for di, dj in zip(dis,djs):
        i2,j2 = i+di, j+dj
        if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and grid[i2][j2]==1:
            visited[i2][j2] = True
            count += 1
            dfs(i2, j2)

result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j] == 1:
            visited[i][j] = True
            count = 1
            dfs(i, j)
            result.append(count)
print(len(result))
result.sort()
print('\n'.join(map(str, result)))