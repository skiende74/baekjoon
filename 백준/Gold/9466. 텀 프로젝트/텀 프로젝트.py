import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+2)
def dfs(i):
    global ans
    j = seq[i]
    if not visited[j]: 
        visited[j] = True
        dfs(j)
    elif not finished[j]:
        k = j
        while k != i:
            k = seq[k]
            ans += 1
        ans += 1
    finished[i] = True     
    
for _ in range(int(input())):
    N = int(input())
    seq = [0]+list(map(int,input().split()))
    visited = [False]*(N+1)
    finished = [False]*(N+1)
    ans = 0
    for i in range(1, N+1):
        if visited[i]: continue
        visited[i] = True
        dfs(i)
    print(N-ans)