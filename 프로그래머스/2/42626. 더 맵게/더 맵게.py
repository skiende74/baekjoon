from heapq import heappush, heappop, heapify
def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while len(scoville) >= 2 and scoville[0] < K:
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a+b*2)
        cnt += 1
    return cnt if scoville[0]>=K else -1