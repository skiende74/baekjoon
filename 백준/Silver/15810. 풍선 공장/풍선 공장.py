# 걸리는시간 -> 풍선개수
def func(time):
    return sum(map(lambda x: time//x, seq))
def lower_bound(goal):
    left, right = 1, goal*max(seq)
    min_idx = right

    while left <= right:
        mid = (left + right)//2

        if func(mid) >= goal:
            right = mid-1
            min_idx = mid
        else: left = mid+1
    return min_idx

N, M = map(int,input().split())
seq = list(map(int,input().split()))
print(lower_bound(M))