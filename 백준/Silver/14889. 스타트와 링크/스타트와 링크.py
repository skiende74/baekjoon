from itertools import combinations

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

ans = 10**9
for comb in combinations(range(N), N//2):
    res = 0
    for a,b in combinations(comb, 2):
        res += grid[a][b] + grid[b][a]
    res2 = 0
    for a,b in combinations(set(range(N))-set(comb), 2):
        res2 += grid[a][b] + grid[b][a]
    ans = min(ans, abs(res-res2))    
print(ans)