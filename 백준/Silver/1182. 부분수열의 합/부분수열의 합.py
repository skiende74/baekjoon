N, S = map(int, input().split())
seq = list(map(int,input().split()))

s = 0
ans = 0
def dfs(i):
    global ans, s
    if i == N: 
        if s == S: 
            ans += 1
        return
    s += seq[i]
    dfs(i+1)
    s -= seq[i]
    dfs(i+1)
dfs(0)
print(ans if S!=0 else ans-1)