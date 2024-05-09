N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

# 1. 섬 식별하기
def dfs(i,j):
    for di,dj in zip([0,0,-1,1], [-1,1,0,0]):
        i2,j2= i+di, j+dj
        if not(0<=i2<N and 0<=j2<M): continue
        if grid[i2][j2] == 1 and not visited[i2][j2]:
            visited[i2][j2] = True
            node.append((i2,j2))
            dfs(i2,j2)

nodes = []
visited = [[False]*(M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] ==1 and not visited[i][j]:
            visited[i][j] = True
            nodes.append([(i,j)])
            node = nodes[-1]
            dfs(i,j)

# 2. 엣지 연결정보 만들기
V = len(nodes)
edges = []
for i in range(V):
    for j in range(i+1,V): # 섬간
        
        min_dist = 10**9 # 섬간 최소거리
        for p1i,p1j in nodes[i]:
            for p2i,p2j in nodes[j]:
                if p1i == p2i: # i동일하면. j연결
                    j1, j2 = min(p1j,p2j), max(p1j,p2j) # 연결로가 바다가 아닌 경우 False
                    is_possible = all([grid[p1i][pj] == 0 for pj in range(j1+1, j2)])
                    
                    if is_possible:
                        min_dist = min(min_dist, j2-j1-1 if j2-j1-1!=1 else 10**9)

                if p1j == p2j: # j동일하면. i연결
                    i1, i2 = min(p1i, p2i), max(p1i,p2i)
                    is_possible = all([grid[pi][p1j] == 0 for pi in range(i1+1, i2)])
                    if is_possible:
                        min_dist = min(min_dist, i2-i1-1 if i2-i1-1!=1 else 10**9)
        
        if min_dist != 10**9:
            edges.append((min_dist,(i,j)))

# 3. MST 구성하기

edges.sort()
parent = [i for i in range(V)]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

cost = 0
count = 0
for d,(i,j) in edges:
    if find(i) != find(j):
        union(i,j)
        cost += d
        count += 1
print(cost if count == V-1 else -1)