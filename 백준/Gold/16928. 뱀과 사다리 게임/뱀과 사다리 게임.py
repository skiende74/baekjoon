
from collections import deque

def bfs(i):
    Q = deque([(i,0)])
    while Q:
        i, d = Q.popleft()

        if i == 100: break
        for j in [j for j in range(i, min(i+6,100)+1)]:
            if dist[j] <= d+1: continue
            dist[j] = d+1
            if snake[j] != j:
                if dist[snake[j]] <= dist[j]: continue
                dist[snake[j]] = dist[j]
                Q.append((snake[j], dist[j]))
                continue
            if ladder[j] != j:
                if dist[ladder[j]] <= dist[j]: continue
                dist[ladder[j]] = dist[j]
                Q.append((ladder[j], dist[j]))
                continue
            Q.append((j, dist[j]))

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
bfs(1)
print(dist[100])