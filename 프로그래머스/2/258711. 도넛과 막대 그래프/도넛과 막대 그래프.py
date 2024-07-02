from collections import defaultdict
graph = defaultdict(lambda: [])
import sys

sys.setrecursionlimit(1000001)
visited = defaultdict(lambda: False)
def solution(edges):
    global visited, has_two, has_cycle
    
    
    for a, b in edges: graph[a].append(b)
    a = {a for a, b in  edges}
    b = {b for a, b in  edges}
    start = list(filter(lambda i: len(graph[i])>=2, a-b))[0]
    result = [start, 0, 0, 0]
    
    for i in graph[start]:
        visited[i] = True
        has_two, has_cycle = False, False
        dfs(i)

        if has_two: result[3] += 1
        elif has_cycle: result[1] += 1
        else: result[2] += 1
    return result

def dfs(i):
    global has_two, has_cycle
    last = i
    if len(graph[i]) >=2: has_two = True
    
    for j in graph[i]:
        if visited[j]: 
            has_cycle = True
            continue
        visited[j] = True
        dfs(j)