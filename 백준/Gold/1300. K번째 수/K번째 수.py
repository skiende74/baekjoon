N = int(input())
k = int(input())

# B[k] (num. 숫자) -> k (몇번째인지)
def func(num):
    k = 0
    for i in range(1,N+1):
        k+= min(N, num//i)
    return k

def lower_bound(k):
    left, right = 0, N**2-1
    min_idx = N**2

    while left <= right:
        mid = (left+right)//2

        if func(mid) >= k:
            right = mid -1
            min_idx = mid
        else: left = mid + 1
    return min_idx
print(lower_bound(k))