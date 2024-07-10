def dfs(i):
    if dp[i] != [INF,INF]: return dp[i]
    dp[i] = [0, 1]
    for j in graph[i]:
        if visited[j]: continue
        visited[j] = True
        dp[i][0] += dfs(j)[1]
        dp[i][1] += min(dfs(j))
    return dp[i]

from collections import defaultdict
import sys
sys.setrecursionlimit(2*10**6)
input = sys.stdin.readline
N = int(input())
graph = defaultdict(lambda: [])
for _ in range(N-1):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

INF = 10**9
dp = [[INF, INF] for _ in range(N+1)]
visited = [False]*(N+1)
visited[1] = True
print(min(dfs(1)))