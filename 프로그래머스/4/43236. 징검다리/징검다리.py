def solution(distance, rocks, n):
    rocks.sort()
    left, right = -1, 10**9+1
    while left+1 < right:
        mid = (left + right) // 2            
        if is_ok(distance, rocks, n, mid): left = mid
        else: right=mid

    return left

def is_ok(distance, rocks, remove_count, condition):
    prev = 0
    res = distance
    for rock in [*rocks, distance]:
        if rock-prev<condition: 
            remove_count -= 1
        else:
            prev = rock
            res = min(res, rock-prev)
    return remove_count>=0
        
            


# 0 2 11 14 17 21 25
#  2 9 3 3 4 4
