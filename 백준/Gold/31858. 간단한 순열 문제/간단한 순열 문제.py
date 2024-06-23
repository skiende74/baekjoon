N = int(input())
seq = list(map(int,input().split()))

ans = N-1
stack = []
for i,s in enumerate(seq):
    while stack and stack[-1][0] <= s and s > 0: 
        ans += 1
        (num, i) = stack.pop()
        if i == 0 : ans -= 1
    if s > 0: stack.append((s,i))
print(ans)