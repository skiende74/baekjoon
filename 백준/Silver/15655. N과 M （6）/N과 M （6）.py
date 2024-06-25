def dfs(i):
    if len(res) == M:
        ans.append(res.copy())
        return
    for j in range(i+1, N):
        res.append(j)
        dfs(j)
        res.pop()

N, M = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()
ans, res  = [], []

dfs(-1)

for res in ans:
    print(' '.join(map(lambda i: str(seq[i]), res)))