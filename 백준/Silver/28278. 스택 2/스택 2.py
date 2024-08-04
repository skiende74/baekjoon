import sys
input = lambda:sys.stdin.readline().rstrip()
N = int(input())
stack = []
for _ in range(N):
    op = input()
    
    if op[0] == '1': stack.append(op[2:])
    elif op[0] == '2': print(stack.pop() if stack else -1)
    elif op[0] == '3': print(len(stack))
    elif op[0] == '4': print(0 if stack else 1)
    else: print(stack[-1] if stack else -1)
