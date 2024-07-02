import sys
input = sys.stdin.readline
N, M  = map(int,input().split())
seq = [int(input()) for _ in range(N)]
seq.sort()

i,j = 0, 1
result = 2*10**9
for i in range(N-1):
    while j<N and seq[j] - seq[i] < M : j += 1
    if j == N: break
    result = min(result, seq[j] - seq[i])
print(result)