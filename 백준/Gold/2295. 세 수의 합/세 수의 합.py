from bisect import bisect_left
import sys
input = sys.stdin.readline
N = int(input())
seq = [int(input()) for _ in range(N)]
seq.sort()

AB = {x+y for x in seq for y in seq}

def solve():
    for l in range(N-1,-1,-1):
        for j in range(l+1):
            if seq[l] - seq[j] in AB:
                return seq[l]
print(solve())