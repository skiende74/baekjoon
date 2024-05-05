import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
prices = [0]+list(map(int,input().split()))

parent = [i for i in range(N+1)]
def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1]=min(r1,r2)
    parent[r2]=min(r1,r2)
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]
for _ in range(M):
    i, j = map(int,input().split())
    union(i,j)
for i in range(1,N+1):
    find(i)

ps = {k:10**9 for k in set(parent[1:])}
for i in range(1,N+1):
    ps[parent[i]]= min(ps[parent[i]], prices[i])
print(sum(ps.values()) if K>=sum(ps.values()) else 'Oh no')
