#123
#200
#3
def fact(n):
    if n==1: return 1
    return n*fact(n-1)

def solve(n, k): # n개중 k번째
    k -= 1
    if n == 1: return [0]    
    
    num = fact(n-1)
    return [k//num, *solve(n-1, k%num+1)]   

def solution(n, k):
    candi = list(range(1, n+1))
    ans = solve(n,k)
    result = []
    for i in ans:
        result.append(candi.pop(i))
    return result
