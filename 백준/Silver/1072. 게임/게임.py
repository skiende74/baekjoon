X, Y = map(int, input().split())
lose = X-Y

left, right = X, X+10**9 # total

winning_rate = (Y*100)//X +1

min_idx = right+1
while left <= right:
    mid = (left + right)//2

    if ((mid-lose)*100)//mid >= winning_rate:
        min_idx = min(min_idx, mid)
        right = mid-1
    else:
        left = mid+1
print(min_idx-X if (min_idx-X) != 10**9+1 else -1)