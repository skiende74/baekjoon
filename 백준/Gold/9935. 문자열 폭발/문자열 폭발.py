seq = input()
bomb = list(input())
M = len(bomb)
stack = []
for s in seq:
    stack.append(s)
    while len(stack)>=M and stack[-M:] == bomb: del stack[-M:]
stack = ''.join(stack)
print(stack if stack else 'FRULA')