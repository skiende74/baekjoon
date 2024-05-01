N, Q = int(input()), int(input())
grid = [0]+[[0]+list(map(int,input().split())) for _ in range(N)]

parent = [i for i in range(N+1)]
def union(i,j):
    r1,r2 = find(i), find(j)
    r = min(r1,r2)
    parent[r1] = r
    parent[r2] = r

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

for i in range(1,N+1):
    for j in range(1, N+1):
        if grid[i][j] == 1: union(i,j)

answer = 'YES'
queries = list(map(int,input().split()))
for i in range(Q-1):
    r1,r2=find(queries[i]), find(queries[i+1])
    if r1 != r2: answer = 'NO'
print(answer)