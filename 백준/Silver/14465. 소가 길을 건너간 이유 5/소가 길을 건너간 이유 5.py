from itertools import accumulate
import sys
input = sys.stdin.readline
N, K, B = map(int,input().split())
light = [1]*(N+1)
for _ in range(B):
    light[int(input())] = 0

p_sum = list(accumulate(light))
min_val = 2*10**5
for i in range(K, N+1):
    min_val = min(min_val, K-(p_sum[i]-p_sum[i-K]))
print(min_val)