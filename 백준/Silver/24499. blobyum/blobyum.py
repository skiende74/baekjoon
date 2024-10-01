N, K = map(int,input().split())
seq = list(map(int,input().split()))
i, j = 0, K%N
val = sum(seq[:K])
ans = val
for _ in range(N):
    val = val + seq[j] - seq[i]
    ans = max(ans, val)
    i, j = (i+1) % N, (j+1) % N
print(ans)