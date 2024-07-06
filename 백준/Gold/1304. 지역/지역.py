N, M = map(int, input().split())

seq = []
for _ in range(M):
    s, e = map(int, input().split())
    if s > e: seq.append((s,e))

for n in range(1, N+1)[::-1]:
    if N%n != 0: continue
    res = True
    d = N//n
    for s,e in seq:
        if (s-1)//d != (e-1)//d:
            res = False
            break
    if res:
        print(n)
        break