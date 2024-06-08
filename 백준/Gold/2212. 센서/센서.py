int(input())
M = int(input())
seq = set(map(int,input().split()))
seq = list(sorted(seq))
N = len(seq)
seq2 = []
prev = seq[0]
for s in seq[1:]:
    seq2.append(s - prev)
    prev = s
seq2.sort()
print(sum(seq2[:N-M]))