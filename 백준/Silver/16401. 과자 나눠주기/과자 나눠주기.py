# 길이 -> 갯수(가능여부)
def func(l):
    return sum(map(lambda x: x//l, seq))

def custom_bound(goal):

    left, right = 1, max(seq)
    max_idx = 0

    while left<=right:
        mid = (left+right)//2
        
        if func(mid) >= goal:
            left = mid + 1
            max_idx = max(max_idx, mid)
        else: right = mid -1
    
    return max_idx

M, N = map(int,input().split())
seq = list(map(int,input().split()))
print(custom_bound(M))