N = 20
times = []
scores = []

def grade2score(g):
    if g=='F': return 0
    return ord('E')-ord(g[0]) + (0.5 if g[1]=='+' else 0)

total = 0
for _ in range(N):
    _, t, s = input().split()
    t = int(float(t))
    if s[0]=='P': continue
    times.append(t)
    total += t*grade2score(s)
print(total/sum(times))