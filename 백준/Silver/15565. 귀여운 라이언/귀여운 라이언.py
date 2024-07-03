from collections import deque

N, K = map(int,input().split())
seq = list(map(int,input().split()))

n = 0
ans = 10**8
Q = deque([])
for i, s in enumerate(seq):
    if s == 1:
        while len(Q) > K-1: Q.popleft()
        Q.append((i, s))
        if len(Q) == K: ans = min(ans, i-Q[0][0]+1)
print(ans if ans != 10**8 else -1)
