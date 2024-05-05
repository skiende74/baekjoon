import sys
input = sys.stdin.readline

N = int(input())
def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1]=min(r1,r2)
    parent[r2]=min(r1,r2)
def find(i):
    if parent[i]==i: return i
    parent[i] = find(parent[i])
    return parent[i]
parent = [i for i in range(N+1)]
for _ in range(N-2):
    i,j = map(int,input().split())
    union(i,j)

for i in range(1, N+1): find(i)

for i in range(1, N+1):
    if parent[i] != 1:
        print(1,i)
        break