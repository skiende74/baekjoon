import sys
input = sys.stdin.readline
N, M, B = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

MIN,MAX = min(map(min, grid)), max(map(max, grid))
def getZ(): 
    min_cost, min_k = 500*500*256*2, 0
    for k in range(MIN, MAX+1):
        add = 0
        remove = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j]<k: add += k-grid[i][j]
                elif grid[i][j]>k: remove += grid[i][j]-k
        if add>remove+B: continue
        cost = add+remove*2
        if cost <= min_cost:
            min_cost = cost
            min_k = k
    print(min_cost, min_k)
getZ()