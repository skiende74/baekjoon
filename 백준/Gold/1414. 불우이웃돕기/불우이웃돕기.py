import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# grid의 문자를 숫자로 변환
def val(x):
    if x=='0': return 0
    
    x = ord(x)
    if x>=ord('a'):
        return x-ord('a')+1
    return x-ord('A')+27

grid = [ list(map(val, list(input()))) for _ in range(N)]

all = sum([ sum(g) for g in grid])

# edges 만들기. 0인건 빼고
edges = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0: continue
        edges.append((grid[i][j],i,j))


# mst 
parent = [i for i in range(N)]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]


cnt = 0
cost = 0
edges.sort()
for d,i,j in edges:
    if find(i) != find(j):
        union(i,j)
        cost += d
        cnt += 1
print(all-cost if cnt == N-1 else -1)