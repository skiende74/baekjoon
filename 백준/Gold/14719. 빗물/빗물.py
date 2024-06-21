N, M = map(int,input().split())
seq = list(map(int,input().split()))

ans = 0
for i in range(1, N+1)[::-1]:
    prev = -1
    for j in range(M):
        if seq[j] >= i:
            if prev != -1: ans += (j-prev-1)
            prev = j
print(ans)           