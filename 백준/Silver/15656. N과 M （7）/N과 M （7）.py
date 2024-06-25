def dfs():
    if len(res) == M:
        ans.append(res.copy())
        return
    for i in range(N):
        res.append(i)
        dfs()
        res.pop()

N, M = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()
ans, res = [], []
dfs()
for res in ans:
    print(' '.join(map(lambda i: str(seq[i]), res)))