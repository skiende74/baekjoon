import sys

input = sys.stdin.readline
N = int(input())
seq = [list(map(int,input().split())) for _ in range(N)]

segments = []
for s, e in seq:
    segments.append((s,1))
    segments.append((e,-1))
segments.sort()

ans, cnt, max_cnt = 0,0,0
for x, op in segments:
    cnt += op
    max_cnt = max(max_cnt, cnt)
print(max_cnt)