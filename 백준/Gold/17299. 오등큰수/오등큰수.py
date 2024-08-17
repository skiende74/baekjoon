from collections import Counter

N = int(input())
seq = list(map(int,input().split()))
V = Counter(seq)
md_stack = []
NGF = [-1]*(N)
for i in range(N):
    while md_stack and V[md_stack[-1][0]] < V[seq[i]]:
        n,j = md_stack.pop()
        NGF[j] = seq[i]
    md_stack.append((seq[i],i))
print(*NGF)