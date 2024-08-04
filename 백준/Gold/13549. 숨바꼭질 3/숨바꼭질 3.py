from collections import deque

A, B = map(int,input().split())
N = 100000
dist = [N+1]*(N+1)
dist[A] = 0

doubled = [False]*(N+1)
def bfs(start):
    global doubled
    Q = deque([start])
    while Q:
        i = Q.popleft()
        if i == B:
            return dist[B]
        
        j = 2*i
        if i != 0 and not doubled[i]:
            while 0<=j<=N:
                if dist[j] == N+1:
                    dist[j] = dist[i]
                    doubled[j] = True
                    Q.append(j)
                j *= 2
        
        for j in [i-1, i+1]:
            if 0<=j<=N and dist[j] == N+1:
                dist[j] = dist[i] + 1
                Q.append(j)
        
print(bfs(A))
