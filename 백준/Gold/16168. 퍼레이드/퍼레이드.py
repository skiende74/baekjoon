def union(i,j):
    r1,r2 = find(i), find(j)
    r1,r2 = min(r1,r2), max(r1,r2)
    parent[r2] = r1
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
parent = [i for i in range(N+1)]
union(0,1)
count = [0 for i in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    count[i] += 1
    count[j] += 1
    union(i,j)
n = len([ i for i in range(1, N+1) if count[i]%2==1])
is_all_connected = len({find(i) for i in range(N+1)}) == 1
print('YES' if ((n==2 or n==0) and is_all_connected) else 'NO')