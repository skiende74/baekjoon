from math import atan2
import sys
input = sys.stdin.readline
N = int(input())
seq = [list(map(int,input().split())) for _ in range(N)]

m = [0,0]
for x, y in seq: m = [m[0]+x, m[1]+y]
m = [m[0]/N, m[1]/N]

for i in range(N): seq[i] = [seq[i][0]-m[0], seq[i][1]-m[1]]

def cross(r1,r2): return r2[1]*r1[0]-r2[0]*r1[1]
ans = 0
for i in range(N):
    ans += (cross(seq[i-1], seq[i]))/2
ans = abs(ans)
print(f'{ans:.1f}')