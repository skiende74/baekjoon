N = 100
grid = [[0]*N for _ in range(N)]
Q = int(input())
coords = [list(map(int,input().split())) for _ in range(Q)]
for x,y in coords:
    for dx in range(10):
        for dy in range(10):
            x2, y2 = x+dx, y+dy
            grid[y2][x2] = 1

print(sum([sum(g) for g in grid]))