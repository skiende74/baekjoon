N = int(input())
seq = list(map(int, input().split()))
seq.sort()

def lower(seq, left, right, goal):
    min_idx = len(seq)+1
    while left <= right:
        mid = (left + right) //2
        if seq[mid] >= goal: 
            min_idx = min(min_idx, mid)
            right = mid-1
        else: left = mid + 1
    return min_idx

def custom(seq, left, right, goal):
    max_idx = -1
    while left <= right:
        mid = (left + right) //2
        if seq[mid] <= goal: 
            max_idx = max(max_idx, mid)
            left = mid + 1
        else: right = mid - 1
    return max_idx

answer = 0
for i in range(N):
    u1 = seq[i]
    for j in range(i+1, N):
        u2 = seq[j]
        u = custom(seq, j+1, N-1,-u1-u2)
        if u1+u2+seq[u]!= 0: continue
        l = max(j+1, lower(seq, j+1, N-1,-u1-u2))
        if u<l: continue
        answer += u-l+1
        #print(u,l)
print(answer)