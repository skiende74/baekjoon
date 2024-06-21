N = int(input())
seq = list(map(int,input().split()))
stack = [(-1,10**8+2)]
ans = [0]*N
for i,s in enumerate(seq):
    while stack and stack[-1][1] <= s: stack.pop()
    if stack: ans[i] = stack[-1][0]
    stack.append((i,s))
print(*[s+1 for s in ans])