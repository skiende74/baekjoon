def possible(m): return (L//m)*(W//m)*(H//m)>=N
N,L,W,H = map(int,input().split())

l, r = 1e-9, min([L,W,H])
for _ in range(10**4):
    m = (l+r)/2
    if possible(m): l = m
    else: r = m
print(f'{l:.10f}')