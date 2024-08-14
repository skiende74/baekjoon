from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [None]*(N+1)
parent[1] = 1
visited = [False]*(N+1)

def dfs(i):
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            parent[j] = i
            dfs(j)

dfs(1)
print('\n'.join(map(str,parent[2:])))