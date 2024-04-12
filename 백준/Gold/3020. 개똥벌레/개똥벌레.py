from itertools import accumulate
from collections import Counter
from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
seq = [int(input()) for _ in range(N)]
max_seq = max(seq)

A = seq[::2]
B = seq[1::2]
A.sort()
B.sort()

def count(seq, target):
    return bisect_right(seq, max_seq) - bisect_left(seq, target)


ans = [10**9, 0]
for h in range(1, H+1):
    c = count(A, h) + count(B, H+1-h)

    if c < ans[0]:
        ans = [c, 1]
    elif c == ans[0]:
        ans[1] += 1
print(' '.join(map(str, ans)))