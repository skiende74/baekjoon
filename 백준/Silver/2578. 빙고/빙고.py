import sys
input = sys.stdin.readline

N = 5
grid = [list(map(int,input().split())) for _ in range(N)]
calls = []
for _ in range(5): 
    calls += list(map(int, input().split()))

pose = {grid[i][j]:(i,j)
 for i in range(N)
    for j in range(N)}

row,col = [5]*N, [5]*N
diag1, diag2= 5,5
cnt = 0
for k,c in enumerate(calls):
    i,j = pose[c]
    row[i] -= 1
    col[j] -= 1
    if row[i] == 0: cnt += 1
    if col[j] == 0: cnt += 1
    if i==j:
        diag1 -= 1
        if diag1 == 0: cnt += 1
    if N-1-i == j:
        diag2 -= 1
        if diag2 == 0: cnt += 1
    if cnt >= 3:
        print(k+1)
        break