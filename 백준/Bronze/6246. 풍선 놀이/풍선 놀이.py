N, Q = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(Q)]

seq = [0]*N
for i,d in queries:
    for j in range(i-1, N, d):
        seq[j] = 1
print(N-sum(seq))