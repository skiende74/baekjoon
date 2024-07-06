import sys
input = sys.stdin.readline
N = int(input())
seq = [list(map(int,input().split())) for _ in range(N)]

segments = []
for s,e in seq:
    segments.append((s,1))
    segments.append((e,-1))

segments.sort()
max_cnt, cnt = 0, 0
prev = 0
for x, op in segments:
    if prev != x: max_cnt = max(max_cnt, cnt)
    cnt += op
    prev = x

print(max_cnt)