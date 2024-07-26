from math import gcd


N = int(input())
seq = [0]+list(map(int,input().split()))
m = min(seq)
ans = 0
left_g = [0]*(N+1)
right_g = [0]*(N+1)

g = 0
for i, s in enumerate(seq):
    g = gcd(g, s)
    left_g[i] = g

g = 0
for i in range(N,0,-1):
    s = seq[i]
    g = gcd(g, s)
    right_g[i] = g

ans_i = -1
for i in range(1,N+1):
    g = gcd(left_g[i-1] if i-1>=1 else 0, right_g[i+1] if i+1<=N else 0)
    if seq[i] % g == 0 : continue
    if g > ans:
        ans = g
        ans_i = i
print(f'{ans} {seq[ans_i]}' if ans else -1)