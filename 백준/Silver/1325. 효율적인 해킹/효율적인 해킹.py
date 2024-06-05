import sys
from collections import deque
input = sys.stdin.readline
def dfs(i):
    global in_cnt
    stack = [i]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if visited[j]: continue
            visited[j] = True
            in_cnt += 1
            stack.append(j)
N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    i,j = map(int, input().split())
    graph[j].append(i)

res = [0]*(N+1)
for i in range(1, N+1):
    visited = [False]*(N+1)
    visited[i]=True
    in_cnt = 1
    dfs(i)
    res[i] = in_cnt
M = max(res)
print(' '.join([str(i) for i,val in enumerate(res) if val==M]))