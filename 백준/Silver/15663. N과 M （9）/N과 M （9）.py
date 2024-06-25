# 순열. seq도 중복 X
def dfs():
    prev = 0
    if len(res) == M:
        ans.append(res.copy())
        return
    
    for j in range(N):
        if visited[j] or seq[j] == prev: continue
        visited[j] = True
        res.append(j)
        prev = seq[j]
        dfs()
        res.pop()
        visited[j] = False


N,M = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()

res, ans = [], []
visited = [False]*N
dfs()

used = set()
for res in ans:
    r = ' '.join(map(lambda i: str(seq[i]), res))
    if r in used: continue
    print(r)
    used.add(r)