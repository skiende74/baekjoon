import sys
input = sys.stdin.readline

def union(i, j):
    r1,r2 = find(i), find(j)
    r1,r2 = min(r1,r2), max(r1,r2)
    parent[r2] = r1
def find(i):
    if parent[i]==i: return i
    parent[i] = find(parent[i])
    return parent[i]

N, M = map(int,input().split())
parent = [i for i in range(N+1)]
cnt = 0
for _ in range(M):
    i, j = map(int,input().split())
    if find(i) == find(j): cnt += 1
    else: union(i,j)
cnt += cnt + N-1-M
print(cnt)