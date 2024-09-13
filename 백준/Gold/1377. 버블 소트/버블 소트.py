import sys
input = sys.stdin.readline
N = int(input())
seq = [(int(input()),i) for i in range(N)]
seq.sort()

print(max([ seq[i][1]-i for i in range(N)])+1)