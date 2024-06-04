from collections import defaultdict
N = int(input())
seq = [list(input()) for _ in range(N)]

dict0 = lambda: defaultdict(lambda: 0)
total = dict0()
for s in seq:
    for i, t in enumerate(s):
        total[t] += 10**(len(s)-i-1)
total = list(sorted(list(total.items()), key = lambda x: -x[1]))
total = list(filter(lambda x: x[1]>0, total))
ans = 0
for i, (t, val) in enumerate(total):
    ans+=(9-i)*val
print(ans)