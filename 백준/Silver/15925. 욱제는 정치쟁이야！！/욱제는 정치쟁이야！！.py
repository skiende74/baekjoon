N, on = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

did = True
did_c = [False]*N
did_r = [False]*N

while did:
    did = False
    for i in range(N):
        if did_r[i]: continue
        do = 1 if sum(grid[i]) > N//2 else 0
        if do != on: continue

        for j in range(N):
            grid[i][j] = on
        did_r[i] = True
        did=True
    for j in range(N):
        if did_c[j]: continue
        do = 1 if sum([grid[i][j] for i in range(N)]) > N//2 else 0
        if do != on: continue

        for i in range(N):
            grid[i][j] = on
        did_c[j] = True
        did = True

def all_set_to():
    for i in range(N):
        for j in range(N):
            if grid[i][j] != on:
                return False
    return True

print(1 if all_set_to() else 0)