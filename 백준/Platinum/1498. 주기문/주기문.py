seq = '#' + input()
N = len(seq)-1

j = -1
f = [-1] + [0]*N
for i in range(1, N+1):
    while j >=0 and seq[i] != seq[j+1] : j = f[j]
    j += 1
    f[i] = j

for i in range(2, N+1):
    unit = i-f[i]
    n = i//unit
    if i % unit != 0: continue
    if n == 1: continue
    print(i, n)