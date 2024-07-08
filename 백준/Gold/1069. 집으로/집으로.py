import sys
input = sys.stdin.readline

X, Y, D, T = map(int, input().split())

d = (X**2 + Y**2)**0.5
t = d
if D/T > 1:
    c = max(d//D-1, 0)
    d -= c*D
    t = c*T + min(d, T+abs(d-D), 2*T)
print(t)