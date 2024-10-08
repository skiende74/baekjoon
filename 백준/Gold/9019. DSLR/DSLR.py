from collections import deque
import sys

input = sys.stdin.readline

alpha = 'DSLR'
def bfs(i):
    Q = deque([i])
    visited = [False]*10000
    visited[i] = True
    while Q:
        i = Q.popleft()
        for k,j in enumerate(graph[i]):
            if visited[j]: continue
            visited[j] = True
            before[j] = i
            a[j] = alpha[k]
            if j == B: return
            Q.append(j)

graph = [[(2*i)%10_000, (i-1)%10_000, (i*10+i//1000)%10_000, (i%10)*1000+i//10] for i in range(10000)]
for _ in range(int(input())):
    A, B = map(int,input().split())

    before = [i for i in range(10000)]
    a = ['']*10000
    bfs(A)
    i = B
    ans = [a[B]]
    while i != before[i]:
        i = before[i]
        ans.append(a[i])
    sys.stdout.write(''.join(ans[::-1])+'\n')