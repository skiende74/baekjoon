from bisect import bisect_left
N = int(input())
seq = list(map(int,input().split()))
selected = [seq[0]]
Index = [0]
for s in seq[1:]:
    if s > selected[-1]: 
        selected.append(s)
        Index.append(len(selected)-1)
    else:
        i = bisect_left(selected,s)
        selected[i] = s
        Index.append(i)


f_i = len(selected)-1
ans = []
for i in range(N-1,-1,-1):
    if Index[i] == f_i:
        f_i -= 1
        ans.append(seq[i])
print(len(ans))
print(*ans[::-1])