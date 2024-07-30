from itertools import combinations
from math import gcd

for _ in range(int(input())):
    seq = list(map(int,input().split()))
    print(max([gcd(i,j) for i, j in combinations(seq, 2)]))