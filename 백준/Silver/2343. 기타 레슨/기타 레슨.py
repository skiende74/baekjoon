N, M = map(int, input().split())
seq = list(map(int,input().split()))

def lower_bound(f, goal):
    left, right = max(seq), sum(seq)
    min_index = sum(seq)

    while left<=right:
        mid = (left + right)//2

        if f(mid) <= goal:
            min_index = min(min_index, mid)
            right = mid-1
        else:
            left = mid+1
    return min_index

# f(강의길이)->강의갯수 단조감소
def f(length):
    sum = 0
    answer = 1
    for s in seq:
        sum += s
        if sum > length:
            sum = s
            answer += 1
    return answer

print(lower_bound(f, M))