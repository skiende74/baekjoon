N = input()
A = list(map(int,input().split()))

stack = []
result = []
for num in A[::-1]:
    while stack and stack[-1] <= num:
        stack.pop()
    result.append(str(stack[-1]) if stack else '-1')
    stack.append(num)
print(' '.join(result[::-1]))