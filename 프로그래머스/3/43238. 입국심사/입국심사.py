def solution(n, times):

    left, right = 1, 10**18
    while left < right:
        mid = (left + right ) // 2
        if is_ok(n, times, mid): right = mid
        else: left = mid+1
    return left
            
    #a, b = 0, 1
    # while not is_ok(n, times, b):
    #     a,b = b, 2*b        
    # while a<b:
    #     m = (a+b)//2
    #     a,b = (a,m) if is_ok(n, times, m) else (m+1,b)
    # return a

def is_ok(n, times, x):
    return n <= sum(x//t for t in times)