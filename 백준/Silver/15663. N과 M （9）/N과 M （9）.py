def dfs():
    prev = 0
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    
    for j in range(N):
        if visited[j] or seq[j] == prev: continue
        visited[j] = True
        res.append(seq[j])
        prev = seq[j]
        dfs()
        res.pop()
        visited[j] = False


N,M = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()

res = []
visited = [False]*N
dfs()