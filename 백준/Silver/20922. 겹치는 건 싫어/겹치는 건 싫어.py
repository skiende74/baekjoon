from collections import defaultdict


N, K = map(int, input().split())
seq = list(map(int,input().split()))

ans = 0
counter = defaultdict(lambda: 0)
counter[seq[0]] = 1
i, j = 0, 0
for i in range(N):
    while j < N-1 and counter[seq[j+1]] < K:
        j += 1
        counter[seq[j]] += 1
    ans = max(ans, j-i+1)

    counter[seq[i]] -= 1
print(ans)