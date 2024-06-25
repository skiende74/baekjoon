def dfs(i):
    if len(res) == M:
        ans.append(res.copy())
        return
    
    for j in range(i, N):
        res.append(j)
        dfs(j)
        res.pop()


N,M = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()

res, ans = [], []
dfs(0)
for res in ans:
    print(' '.join(map(lambda i: str(seq[i]), res)))