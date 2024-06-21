N = int(input())
seq = list(map(int,input().split()))
stack = []
ans = [-1]*N
for i,s in enumerate(seq):
    while stack and seq[stack[-1]] <= s: stack.pop()
    if stack: ans[i] = stack[-1]
    stack.append(i)
print(*[s+1 for s in ans])