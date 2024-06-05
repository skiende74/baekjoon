def gcd(a,b):
    if b==0: return a
    return gcd(b, a%b)


def solve(N):
    num, den = N, N
    for i in range(2, N+1):
        num, den = num*i+den, den*i
        g = gcd(num,den)
        num //= g
        den //= g

    num *= N
    g = gcd(num,den)
    num //= g
    den //= g

    # den,num = num,den
    if den == 1: print(num)
    else:
        q, r = divmod(num, den)

        l1 = len(str(r))
        l2 = len(str(den))
        A = len(str(q))
        a=' '*(A+1)+str(r)
        b=str(q)+' '+ '-'*max(l1,l2)
        c=' '*(A+1)+str(den)
        print(a)
        print(b)
        print(c)

import sys
input = sys.stdin.read
data = input().splitlines()

for N in data:
    if N.strip():
        solve(int(N))