# 순열. seq도 중복 X
def dfs():
    if len(res) == M:
        ans.append(res.copy())
        return
    
    for j in range(N):
        if j in res: continue
        res.append(j)
        dfs()
        res.pop()

N,M = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()

res, ans = [], []
dfs()

used = set()
for res in ans:
    r = ' '.join(map(lambda i: str(seq[i]), res))
    if r in used: continue
    print(r)
    used.add(r)