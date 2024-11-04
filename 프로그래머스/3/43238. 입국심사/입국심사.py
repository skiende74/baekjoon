def solution(n, times):

    left, right = 1, 10**18
    while left+1 < right:
        mid = (left + right) // 2
        if is_ok(n, times, mid): right = mid
        else: left = mid
    return right
            

def is_ok(n, times, x):
    return n <= sum(x//t for t in times)