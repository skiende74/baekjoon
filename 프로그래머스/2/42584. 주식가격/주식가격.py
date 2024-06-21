def solution(prices):
    N = len(prices)
    answers = [0]*N
    stack = [(0, N-1)]
    for i in range(N-1, -1, -1):
        p = prices[i]
        while stack and stack[-1][0] >= p: stack.pop()
        answers[i] = stack[-1][1]-i
        stack.append((p, i))
    
    return answers