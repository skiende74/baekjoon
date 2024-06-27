def union(i,j):
    r1, r2 = find(i),find(j)
    r1, r2 = min(r1,r2), max(r1,r2)
    parent[r2] = r1
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

N, Q = map(int,input().split())
lines = [[i, *list(map(int,input().split()))[:-1]] for i in range(N)]
lines.sort(key=lambda x: (x[1],x[2]))

parent = list(range(N))
prev = lines[0]
for i, s,e in lines:
    if prev[2] >= s:
        union(i, prev[0])
    prev = i,s,e

for _ in range(Q):
    i,j = map(int,input().split())
    print(1 if find(i-1)==find(j-1) else 0)

