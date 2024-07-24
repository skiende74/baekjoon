from itertools import accumulate
import sys
input =sys.stdin.readline
N = int(input())
seq = [0] + list(map(int,input().split()))
p_sum = list(accumulate(seq))
for _ in range(int(input())):
    i, j = map(int,input().split())
    print(p_sum[j]-p_sum[i-1])