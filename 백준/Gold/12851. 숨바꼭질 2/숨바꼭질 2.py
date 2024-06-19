from collections import deque
N = 10**5
dist = [10**6]*(N+1)
count = [0]*(N+1)
def bfs(start):
    dist[start] = 0
    count[start] = 1
    Q = deque([start])
    while Q:
        i = Q.popleft()
        for j in (2*i, i-1, i+1):
            if 0<=j<=N and dist[j] >= dist[i]+1: # ( 경로합치기위해선 재방문도 필요 )
                if dist[j] == 10**6:  Q.append(j) # 딱한번만 큐에넣는다. 그리고 끝나지 않았을때만.
                dist[j] = dist[i] + 1
                count[j] += count[i]
s, e = map(int,input().split())
bfs(s)
print(dist[e])
print(count[e])