from bisect import bisect_left
N = int(input())
seq = list(map(int,input().split()))
selected = [seq[0]]
for s in seq[1:]:
    if s > selected[-1]: selected.append(s)
    else:
        i = bisect_left(selected,s)
        selected[i] = s
print(len(selected))