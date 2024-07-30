from math import gcd, prod
input()
a = prod(map(int, input().split()))
input()
b = prod(map(int,input().split()))
ans = gcd(a,b)
print(ans if ans<10**9 else str(ans)[-9:])