N, M = map(int,input().split())
seq = list(map(int,input().split()))

left, right = 0, max(seq)
while left <= right:
    mid = (left + right)//2

    res = 0
    res = sum(map(lambda x: x-mid, filter(lambda x: x>mid, seq)))
    #for s in seq:
    #    res += max(0, s-mid)
    if res < M:
        right = mid-1
    else:
        left = mid+1
print(right)


