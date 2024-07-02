from collections import defaultdict
graph = defaultdict(lambda: [])
import sys
sys.setrecursionlimit(1000001)

def solution(edges):
    global visited, has_two_path
    result = [-1,0,0,0]
    N = -1
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        N = max(N, a, b)
        
    toward = [True]+[False]*(N)
    for edge in edges:
        a, b = edge
        toward[b] = True
    
    
    for i, t in enumerate(toward):
        if not t and len(graph[i]) >= 2:
            result[0] = i
            break
    
    visited = [False]*(N+1)
    for i in graph[result[0]]:
        if not visited[i]:
            has_two_path = False
            dfs(i)
            if len(graph[i]) == 2:
                result[3] +=1
            elif len(graph[i]) == 1:
                if visited[i]:
                    if has_two_path:
                        result[3] += 1
                    else:
                        result[1] += 1
                else:
                    result[2] += 1
            elif len(graph[i]) == 0:
                result[2] += 1
            visited[i] = True
    return result

def dfs(i):
    global has_two_path
    if len(graph[i]) >=2:
        has_two_path = True
    for j in graph[i]:
        if visited[j]: continue
        visited[j] = True
        dfs(j)
    