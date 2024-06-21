seq = input()
bomb = list(input())
M = len(bomb)
stack = []
for s in seq:
    stack.append(s)
    while len(stack)>=M and stack[-1] == bomb[-1] and stack[-M:] == bomb:
        for _ in range(M): stack.pop()

stack = ''.join(stack)
print(stack if stack else 'FRULA')