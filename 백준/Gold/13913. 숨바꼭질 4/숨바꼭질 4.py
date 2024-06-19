from collections import deque
N = 10**5
visited = [False]*(N+1)
move = [i for i in range(N+1)]
def bfs(start):
    Q = deque([start])
    visited[start] = True
    while Q:
        i = Q.popleft()
        if i == e: return i
        for j in [2*i, i-1, i+1]:
            if 0<=j<=10**5 and not visited[j]:
                visited[j] = True
                Q.append(j)
                if move[j] == j: move[j] = i
    return N+2

def find(j):
    ans = [j]
    while j != s:
        j = move[j]
        ans.append(j)
    return ans[::-1]

s, e = map(int,input().split())

j = bfs(s)
ans = find(j)
print(len(ans)-1)
print(*ans)
