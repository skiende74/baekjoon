from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
start = Counter(input() for _ in range(N))
end = Counter(input() for _ in range(N-1))

print((start-end).most_common()[0][0])