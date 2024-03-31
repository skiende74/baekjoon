N = int(input())
grid=[list(map(int, input().split())) for _ in range(N)]

diag1 = [False]*(2*N-1)
diag2 = [False]*(2*N-1)

def dfs(k):
    global inner_count, max_inner_count

    if k>=M: 
        max_inner_count = max(max_inner_count, inner_count)
        return
    # 가지치기
    if max_inner_count >= (inner_count + (M+1-k)//2): 
        return

    for i,j in jobs[k]:
        if not diag2[i-j]:
            inner_count += 1
            # max_inner_count = max(max_inner_count, inner_count)
            diag2[i-j] = True
            dfs(k+2)
            diag2[i-j] = False 
            inner_count -= 1
    dfs(k+2)
    

M = 2*N-1
jobs = [[] for _ in range(M)]
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            jobs[i+j].append((i,j))

inner_count = 0
max_inner_count = 0

answer = 0

dfs(0)
answer += max_inner_count
max_inner_count = 0
dfs(1)
answer += max_inner_count
print(answer)