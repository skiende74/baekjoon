def solve(n, wires):
    visited = [True] + [False]*(n)
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    ans = []
    def dfs(i):
        nonlocal cnt
        for j in graph[i]:
            if visited[j]: continue
            visited[j] = True
            cnt += 1
            dfs(j)
    
    for i in range(1, n+1):
        if visited[i]: continue
        visited[i] = True
        cnt = 1
        dfs(i)
        ans.append(cnt)
    return abs(ans[0]-ans[1])
    
def solution(n, wires):
    return min([ solve(n, [*wires[:k], *wires[k+1:]]) for k in range(n-1)])
    
