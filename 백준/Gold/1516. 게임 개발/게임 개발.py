from collections import deque
import sys
input = sys.stdin.readline

V = int(input())

# 전처리 (graph, indegree 만들기. times도.)
indegree = [0]*(V+1)
times = [0]*(V+1)
graph = [[] for _ in range(V+1)]
for i in range(1, V+1):
    t, *p, _ = map(int,input().split())
    for pp in p:
        graph[pp].append(i)
        indegree[i] += 1
    times[i] = t    

# 위상정렬
Q = deque([i for i in range(1,V+1) if indegree[i] == 0])
result = [-1 for _ in range(V+1)]

start_time = times.copy()
while Q:
    i = Q.popleft()
    for j in graph[i]:
        indegree[j] -= 1
        start_time[j] = max(start_time[j], start_time[i]+times[j])
        if indegree[j] == 0:
            Q.append(j)
            
print(*start_time[1:], sep='\n')