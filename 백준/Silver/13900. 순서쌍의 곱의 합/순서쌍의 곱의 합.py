from itertools import accumulate
N= int(input())
seq = list(map(int,input().split()))
p_sum = list(accumulate(seq))
ans = 0
for i in range(1, N):
    ans += p_sum[i-1]*seq[i]
print(ans)