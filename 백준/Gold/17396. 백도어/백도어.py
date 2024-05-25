from heapq import heappush, heappop
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
seq = list(map(int,input().split()))
seq[-1] = 0
edges = [ list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(V)]
for i, j, w in edges:
    if seq[i] or seq[j]: continue
    graph[i].append((j, w))
    graph[j].append((i, w))

def dijkstra(S):
    dist = [10**11]*V
    dist[S] = 0
    PQ = [(dist[S], S)]
    while PQ:
        d, i = heappop(PQ)
        if dist[i] < d: continue
        
        for j, w in graph[i]:
            if dist[j] > d + w:
                dist[j] = d + w
                heappush(PQ, (dist[j], j))
    return dist
dist = dijkstra(0)
print(dist[-1] if dist[-1] != 10**11 else -1)