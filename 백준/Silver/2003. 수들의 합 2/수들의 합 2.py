from itertools import accumulate
N, M = map(int,input().split())
seq = [0] + list(map(int,input().split()))
prefix_sum = list(accumulate(seq))

j = 0
ans = 0
for i in range(N+1):
    while prefix_sum[j]-prefix_sum[i]<M and j<N: j += 1
    if prefix_sum[j]-prefix_sum[i] == M: ans += 1
print(ans)