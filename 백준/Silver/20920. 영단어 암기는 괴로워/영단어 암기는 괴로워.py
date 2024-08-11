from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

counter = Counter([ input() for _ in range(N)])
print('\n'.join(filter(lambda x: len(x)>=M, sorted(counter, key=lambda x: (-counter[x], -len(x), x)))))