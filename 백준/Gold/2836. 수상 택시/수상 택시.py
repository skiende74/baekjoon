import sys
input = sys.stdin.readline
N, M = map(int,input().split())

seq = list(filter(lambda x: x[0]>x[1], [list(map(int,input().split())) for _ in range(N)]))

segments = []
for s, e in seq:
    segments.append((s, -1))
    segments.append((e, 1))

segments.sort()

ans, cnt = 0, 0
for x, op in segments:
    if cnt: ans += x-prev
    cnt += op
    prev = x
print(M + ans*2)