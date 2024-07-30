from itertools import permutations
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    seq = list(map(int,input().split()))
    seq.sort()
    left, right = [], []
    for i in range(len(seq)):
        if i % 2 == 0: left.append(seq[i])
        else: right.append(seq[i])
    seq2 = left + right[::-1]
    print(
        max([
            abs(seq2[i]-seq2[i-1])
            for i in range(N)
             ]))