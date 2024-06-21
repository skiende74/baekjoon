seq = input()
bomb = list(input())
M = len(bomb)
b = bomb[-1]
stack = []
for s in seq:
    stack.append(s)
    while s==b and stack[-M:] == bomb: del stack[-M:]
print(''.join(stack) if stack else 'FRULA')