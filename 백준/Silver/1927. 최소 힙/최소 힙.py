from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
PQ = []
for _ in range(N):
    n = int(input())
    if n == 0: print(heappop(PQ) if PQ else 0)
    else: heappush(PQ, n)