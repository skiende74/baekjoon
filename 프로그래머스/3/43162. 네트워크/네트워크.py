def solution(n, computers):
    def dfs(i):
        for c,v in enumerate(computers[i]):
            if visited[c] or not(v): continue
            visited[c] = True
            dfs(c)
    
    visited = [False]*n
    answer = 0
    for i in range(n):
        if visited[i]:continue
        visited[i] = True
        dfs(i)
        answer+=1
    return answer