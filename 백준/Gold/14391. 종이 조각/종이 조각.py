N, M = map(int,input().split())
grid = [list(map(int, list(input()))) for _ in range(N)]

ans = 0
for idx in range(1<<(N*M)):
    row_sum, col_sum = 0, 0
    total = 0
    for i in range(N):
        row_sum = 0
        for j in range(M):
            if (idx & 1<<(i*M+j)) == 0:
                row_sum = row_sum*10 + grid[i][j]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum
    
    for j in range(M):
        col_sum = 0
        for i in range(N):
            if (idx & 1<<(i*M+j)) != 0:
                col_sum = col_sum*10 + grid[i][j]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    ans = max(ans, total)
print(ans)
    