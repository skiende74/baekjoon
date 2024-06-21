def solution(number, k):
    N = len(number)
    number = list(map(int, list(number)))
    stack = []
    cnt = 0
    for s in number:
        while cnt < k and stack and stack[-1] < s:
            stack.pop()
            cnt += 1
        stack.append(s)
    if cnt<k: stack = stack[:-(k-cnt)]
    return ''.join(map(str, stack))