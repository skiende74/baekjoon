from heapq import heappush, heappop
import sys 

input = sys.stdin.readline

INF = 10**9
def dijkstra(start):
    dist = [INF]*(V+1)
    dist[start]=0

    PQ = [(0, start)]
    while PQ:
        d, i = heappop(PQ)
        if dist[i] < d: continue

        for j,w in graph[i]:
            if dist[j] <= d+w: continue
            
            dist[j] = d+w
            heappush(PQ, (d+w, j))
    return dist

T = int(input())
for _ in range(T):
    V, E, t = map(int,input().split())
    start, g, h = map(int,input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        i,j,w = map(int,input().split())
        graph[i].append((j,w))
        graph[j].append((i,w))

    ends = [int(input()) for _ in range(t)]

    dist = dijkstra(start)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    answer = []
    for e in ends:
        if dist[e] == dist[g]+dist_g[h]+dist_h[e] or dist[e] == dist[h]+dist_h[g]+dist_g[e]:
            answer.append(e)
    answer.sort()
    for ans in answer:
        print(ans, end=' ')