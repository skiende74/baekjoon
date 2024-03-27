import heapq
import sys

pq=[]
for _ in range(int(input())):
    x = int(sys.stdin.readline().rstrip() )
    if x != 0:
        heapq.heappush(pq, (abs(x),x))
    else:
        print(heapq.heappop(pq)[1] if pq else 0)
