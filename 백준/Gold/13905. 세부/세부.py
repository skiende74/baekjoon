import sys
input = sys.stdin.readline
from heapq import heappush, heappop
V, E = map(int,input().split())
s, e =map(int,input().split())
INF = 10**9
graph = [[] for _ in range(V+1)]
for _ in range(E):
    i,j, w = map(int,input().split())
    graph[i].append((j, w))
    graph[j].append((i, w))
    

dist = [0]*(V+1)
def dijkstra(start):
    PQ = [(-INF,start)]
    dist[start] = INF
    while PQ:
        d, i= heappop(PQ)
        d = -d
        # print(1)
        for j,w in graph[i]:
            # print(f'j:{j} {dist[j]},{d},{w}')
            if dist[j] >= min(d, w): continue
            dist[j] = min(d, w)
            heappush(PQ, (-dist[j],j))

dijkstra(s)
print(dist[e])
# print(dist)