N, M = map(int,input().split())
seq = [int(input()) for _ in range(N)]
max_seq = max(seq)
# 금액 -> 횟수
def count(money):
    result = 0
    cur = 0
    for s in seq:
        if s > cur:
            cur = money
            result += 1
        cur -= s
    return result

def lower_bound(M):
    left, right = max_seq, sum(seq)
    min_idx = right

    while left <= right:
        mid = (left+right)//2
        if count(mid) <= M:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else: left = mid + 1
    return min_idx

print(lower_bound(M))