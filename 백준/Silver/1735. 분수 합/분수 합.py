from math import gcd


a, b = map(int,input().split())
c, d = map(int,input().split())

A, B = a*d+b*c, b*d
g = gcd(A,B)
print(A//g, B//g)