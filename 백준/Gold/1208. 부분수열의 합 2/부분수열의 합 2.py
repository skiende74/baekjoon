from bisect import bisect_left, bisect_right
from itertools import combinations

N, M = map(int, input().split())
seq = list(map(int,input().split()))

def count(subset, target) -> int:
    return bisect_right(subset, target) - bisect_left(subset,target)
def calc_subset(seq) ->None:
    return [sum(comb) for i in range(1, len(seq)+1)
        for comb in combinations(seq, i)]
    
def solve()->int:
    x = calc_subset(seq[:N//2])
    y = calc_subset(seq[N//2:])

    x.sort()
    y.sort()

    cnt = 0
    for i in x:
        cnt += count(y, M-i)
    cnt += count(x, M) + count(y,M)

    return cnt
print(solve())
    