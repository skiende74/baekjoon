N, M = map(int,input().split())
r,c,d = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
cleans = set()
def in_range(i,j):
    return 0<=i<N and 0<=j<M and grid[i][j]==0
i,j = r,c
dir = [[-1,0],[0,1],[1,0],[0,-1]]
for _ in range(10000):
    cleans.add((i,j)) # 1
    not_clean = [(i+di,j+dj) for di,dj in zip([0,0,-1,1],[-1,1,0,0]) if in_range(i+di,j+dj) and (i+di,j+dj) not in cleans]
    if not_clean: # 3. 청소되지 않은 칸 있으면, 반시계 회전 + 앞칸이 청소안되었으면 전진
        d = (d-1)%4
        di,dj = dir[d]
        next = i+di, j+dj
        if next in not_clean: i,j = next
    else: # 2 청소된
        di, dj = dir[(d-2)%4]
        next = i+di, j+dj
        if in_range(*next):
            i, j = next
        else: 

            break
print(len(cleans))