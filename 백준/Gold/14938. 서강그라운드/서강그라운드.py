from heapq import heappush, heappop
import sys

input = sys.stdin.readline

V, M, E = map(int,input().split())

st = 2

item = [0]+list(map(int, input().split()))
graph = [[] for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    graph[i].append((j,w))
    graph[j].append((i,w))
INF = 10**9


def dijkstra(st):
    dist = [INF]*(V+1)
    dist[st] = 0
    PQ = [(0, st)]

    while PQ:
        d, i = heappop(PQ)
        if dist[i] < d: continue

        for j, w in graph[i]:
            if dist[j] > d+w:
                dist[j] = d+w
                heappush(PQ, (dist[j], j))
    ans = []  
    for i in range(1,V+1):
        if dist[i] <= M:
            ans.append(item[i])
    return sum(ans)

answer = -1
for i in range(1, V+1):
    answer = max(answer, dijkstra(i))
print(answer)