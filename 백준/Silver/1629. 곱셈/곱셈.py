A,B,C = map(int,input().split())
A %= C

def solve(A,B,C):
    if B==1: return A
    ans = 1 if B % 2 == 0 else A
    return (ans*solve((A*A)%C, B//2, C))%C
print(solve(A,B,C))