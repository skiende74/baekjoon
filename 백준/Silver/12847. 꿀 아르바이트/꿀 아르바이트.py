from itertools import accumulate
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
seq = [0] + list(map(int,input().split()))
p_sum = list(accumulate(seq))

ans = 0
for i in range(M, N+1):
    ans = max(ans, p_sum[i]-p_sum[i-M])
print(ans)