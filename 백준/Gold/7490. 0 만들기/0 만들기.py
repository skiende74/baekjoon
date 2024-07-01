def dfs(i):
    global result
    if i==N-1: 
        result.append(res.copy())
        return
    for op in [' ', '+','-']:
        res.append(op)
        dfs(i+1)
        res.pop()

def print_op(op):
    res = '1'
    for i in range(2, N+1):
        res += op[i-2]+str(i)
    print(res)
total = 0
nums = []
for _ in range(int(input())):
    N = int(input())

    res,result = [],[]
    dfs(0)
    ops = result
    for op in ops:
        total,prev = 1, 1
        for i in range(2,N+1):
            if op[i-2]=='+': prev = i
            elif op[i-2]=='-': prev = -i
            else: 
                total -= prev
                prev = (prev//abs(prev))*(abs(prev)*10+i)
            total += prev
        if total == 0: print_op(op)
    print()