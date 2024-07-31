N = int(input())
seq = []
for i, s in enumerate(map(int,input().split())):
    seq.append((i+1, s))

i = 0
answer = []
while seq:
    j, di = seq.pop(i)
    answer.append(j)
    if seq: i = (i + di + (-1 if di>0 else 0)) % len(seq)
print(' '.join(map(str, answer)))