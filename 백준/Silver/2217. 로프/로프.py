import sys
input = sys.stdin.readline
N = int(input())
seq = [int(input()) for _ in range(N)]
seq.sort()

total = 0
for i, s in enumerate(seq):
    total = max(total, (N-i)*s)
print(total)