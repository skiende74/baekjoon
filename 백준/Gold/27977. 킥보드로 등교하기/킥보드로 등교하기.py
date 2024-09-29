L, N, K = map(int,input().split())
seq = [0]+list(map(int,input().split()))+[L]

def is_possible(battery):
    cnt = 0
    s_old = 0
    for i in range(len(seq)):
        if seq[i]-s_old > battery:
            s_old = seq[i-1]
            cnt += 1
            if seq[i]-s_old > battery: return False
    return K >= cnt

l, r = 0, L
while l < r:
    mid = (l + r) // 2
    if is_possible(mid): r = mid
    else: l = mid + 1
print(l)