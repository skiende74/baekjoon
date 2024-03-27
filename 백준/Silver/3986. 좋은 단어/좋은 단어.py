import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
answer = 0

for _ in range(N):
    seq = list(input())
    stack = []
    for s in seq:
        if len(stack)>0 and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if len(stack)==0:
        answer += 1

print(answer)