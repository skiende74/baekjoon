from collections import deque
def solution(l, weight, weights):
    weights = deque(weights)
    bridges = deque([0]*l)
    cnt = 0
    w = 0
    while weights:
        w -= bridges[0]
        bridges.popleft()
        bridges.append(0)
        if w+weights[0] <= weight:
            bridges[-1] = weights.popleft()
            w += bridges[-1]
        cnt += 1
    cnt2 = 0
    for i in range(l):
        if bridges[i] > 0: cnt2 = i+1
    return cnt + cnt2