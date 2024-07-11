import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+10)

def union(i,j):
    r1,r2 = find(i),find(j)
    r1, r2 = min(r1,r2), max(r1,r2)
    parent[r2] = r1

def find(i):
    if parent[i]==i: return i
    parent[i] = find(parent[i])
    return parent[i]

N = int(input())

parent = [i for i in range(N+1)]
M = int(input())
for _ in range(M):
    i, j = map(int,input().split())
    while i<=j-1:
        union(j-1,j)
        j = find(j)
for i in range(1,N+1): find(i)
print(len(set(parent[1:])))
    