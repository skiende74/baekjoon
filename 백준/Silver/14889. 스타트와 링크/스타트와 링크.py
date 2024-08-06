def dfs(i):
    global total, ans
    if len(selected) == N//2:
        ans = min(ans, abs(total))
        return
    for j in range(i, N):
        diff = sum(grid[j][k] + grid[k][j] for k in range(N))
        selected.add(j)
        total += diff
        dfs(j+1)
        total -= diff
        selected.remove(j)


N = int(input())
grid = [ list(map(int,input().split())) for _ in range(N) ]

selected = set(range(N))
total = -sum(map(sum, grid))
ans = 10**9
dfs(0)
print(ans)