from heapq import heappop, heappush
def dijkstra(i):
    PQ = [(0, i)]
    while PQ:
        d, i = heappop(PQ)
        for j in [ j for j in range(i+1, min(i+6, 100)+1)]:
            if dist[j] <= d+1: continue
            dist[j] = d+1
            if snake[j] != j:
                if dist[snake[j]] > dist[j]: 
                    dist[snake[j]] = dist[j]
                    heappush(PQ, (dist[j], snake[j]))
                continue
            if ladder[j] != j:
                if dist[ladder[j]] > dist[j]: 
                    dist[ladder[j]] = dist[j]
                    heappush(PQ, (dist[j], ladder[j]))
                continue
            heappush(PQ, (d+1, j))
import sys
input = sys.stdin.readline
M, K = map(int,input().split())
ladder, snake = [i for i in range(101)], [i for i in range(101)]
for _ in range(M):
    i, j = map(int,input().split())
    ladder[i] = j
for _ in range(K):
    i, j = map(int,input().split())
    snake[i] = j

dist = [1000]*101
dist[1] = 0
dijkstra(1)
print(dist[100])