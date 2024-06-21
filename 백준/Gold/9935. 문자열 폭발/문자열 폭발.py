seq = input()
bomb = list(input())
M = len(bomb)
b = bomb[-1]
stack = []
for s in seq:
    stack.append(s)
    while s==b and stack[-M:] == bomb: del stack[-M:]
stack = ''.join(stack)
print(stack if stack else 'FRULA')