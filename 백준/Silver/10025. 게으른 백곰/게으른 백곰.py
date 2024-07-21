import sys
input = sys.stdin.readline
M, K = map(int,input().split())
N = 1_000_000
ices = [0]*(N+1)
for _ in range(M):
    g, x = map(int, input().split())
    ices[x] += g

val = sum(ices[:2*K+1])
max_val = val
for i in range(2*K+1, N+1):
    val += ices[i] - ices[i-2*K-1]
    max_val = max(max_val, val) 
print(max_val)