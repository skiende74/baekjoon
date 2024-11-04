def solution(prices):
    N = len(prices)
    prices[-1]=(-1)
    answer = [0]*N
    stack = [(prices[0], 0)]
    for i in range(1, N):
        while stack and stack[-1][0] > prices[i]:
            el = stack.pop()
            answer[el[1]] = i-el[1]
        stack.append((prices[i], i))
    return answer