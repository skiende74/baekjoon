import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())

# 그래프 딕셔너리 G 생성
G = defaultdict(list)
for _ in range(N-1):
    i, j = map(int, input().split())
    G[i].append(j)
    G[j].append(i)

def bfs(start:int) -> list:
    result = [-1] * (N + 1)
    queue = deque()
    result[start]=0
    queue.append(start)
    while queue: #  BFS
        node = queue.popleft()
        # 자식 탐색
        for c in G[node]:
            if result[c] == -1: # 미탐색
                result[c] = result[node] + 1
                queue.append(c)
    
    return result

a, b, c = map(int,input().split())
A, B, C = bfs(a), bfs(b), bfs(c)

result = False
for i in range(1, N+1):
    if len(G[i])==1: # 리프노드
        if A[i] < B[i] and A[i] < C[i]:
            result = True
            
print('YES' if result else 'NO')