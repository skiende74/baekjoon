from collections import defaultdict
from heapq import heappush, heappop
def solution(operations):
    counter = defaultdict(lambda: 0) 
    min_heap, max_heap = [], []
    for op in operations:
        o, num = op.split()
        num = int(num)
        
        if o == 'I':
            counter[num] += 1
            heappush(min_heap, num)
            heappush(max_heap, -num)
        else:
            if num == 1:
                while max_heap:
                    n = -heappop(max_heap)
                    if counter[n] > 0:
                        counter[n] -= 1
                        break
            else:
                while min_heap:
                    n = heappop(min_heap)
                    if counter[n] > 0:
                        counter[n] -= 1
                        break
    m, M = 0, 0
    while max_heap:
        n = -heappop(max_heap)
        if counter[n] >0:
            M = n
    while min_heap:
        n = heappop(min_heap)
        if counter[n] >0:
            m = n
    
    return [ m, M]
