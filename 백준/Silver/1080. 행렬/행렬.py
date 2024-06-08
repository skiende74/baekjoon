N, M = map(int,input().split())
grid = [list(map(int,list(input()))) for _ in range(N)]
goal = [list(map(int,list(input()))) for _ in range(N)]


cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if grid[i][j] == goal[i][j]: continue
        for i2 in range(i,i+3):
            for j2 in range(j,j+3):
                grid[i2][j2] = 1- grid[i2][j2]
        cnt += 1

is_possible = all([grid[i][j] == goal[i][j] for i in range(N)
    for j in range(M)])
print(cnt if is_possible else -1)