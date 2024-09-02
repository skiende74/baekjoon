from heapq import heapify, heappop, heappush

n, m = map(int,input().split())
seq = list(map(int,input().split()))
heapify(seq)
for _ in range(m):
    a = heappop(seq)
    b = heappop(seq)
    heappush(seq, a+b)
    heappush(seq, a+b)
print(sum(seq))