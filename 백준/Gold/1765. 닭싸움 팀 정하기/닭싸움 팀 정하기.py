import sys
input = sys.stdin.readline

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]
def union(i, j):
    r1, r2 = find(i), find(j)
    r1, r2 = min(r1,r2), max(r1,r2)
    parent[r2] = r1

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    com, i, j = input().split()
    i, j = int(i), int(j)
    if com == 'F': union(i,j)
    else:
        if graph[i]: union(graph[i][0], j)
        graph[i].append(j)
        if graph[j]: union(graph[j][0], i)
        graph[j].append(i)

for i in range(1,N+1): find(i)
print(len(set(parent[1:])))