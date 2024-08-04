N = int(input())
seq = list(map(int,input().split()))

stack = []
turn = 1
for s in seq:
    if s != seq: stack.append(s)
    else: turn += 1
    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

print('Nice' if turn==N+1 else 'Sad')