from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global ans
    if color[start] == 0: color[start]=-1
    Q = deque([(start, color[start])])
    while Q:
        i, r = Q.popleft()
        for j in graph[i]:
            if color[j]*color[i] == 1: 
                ans = 'NO'
                return
            if color[j] == 0:
                color[j] = -r
                Q.append((j,-r))
for _ in range(int(input())):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int,input().split())
        graph[i].append(j)
        graph[j].append(i)
    
    ans = 'YES'
    color = [0]*(V+1)
    for i in range(1,V+1):
        bfs(i)
    print(ans)
    