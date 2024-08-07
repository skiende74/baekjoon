
from collections import deque


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
input()
C = list(map(int,input().split()))

ans = []
B = deque([B[i] for i in range(N) if A[i] == 0])
for c in C:
    B.appendleft(c)
    ans.append(B.pop())
print(*ans)
