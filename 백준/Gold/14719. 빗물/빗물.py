N, M = map(int,input().split())
seq = list(map(int,input().split()))

ans = 0
stack = []

for i, s in enumerate(seq):
    while stack and seq[stack[-1]]<=s:
        j = stack.pop()
        if not stack: continue
        ans += (min(s,seq[stack[-1]])-seq[j])*(i-stack[-1]-1)
    stack.append(i)
print(ans)