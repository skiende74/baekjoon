def dfs(i):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    for j in range(i,N+1):
        ans.append(j)
        dfs(j)
        ans.pop()

N, M = map(int,input().split())
ans = []
dfs(1)