import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, Q = map(int,input().split())

parent = [i for i in range(N+1)]
def union(i,j):
    r1, r2 =  find(i),find(j)
    r = min(r1, r2)
    parent[r1] = r
    parent[r2] = r
def find(i):
    if parent[i] == i: return i
    parent[i] =  find(parent[i])
    return parent[i]

for _ in range(Q):
    op, a, b = map(int,input().split())
    if op == 0: union(a,b)
    else:  print('YES' if find(a) == find(b) else 'NO')
print(parent)