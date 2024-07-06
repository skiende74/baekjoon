import sys
input = sys.stdin.readline
N = int(input())
seq = [list(map(int,input().split())) for _ in range(N)]

segments = []
for s,e in seq:
    segments.append((s,1))
    segments.append((e,-1))

segments.sort()
cnt = 0
prev = segments[0][0]
ans = 0
for x, op in segments:
    if cnt: ans += x-prev
    cnt += op
    prev = x
    
print(ans)