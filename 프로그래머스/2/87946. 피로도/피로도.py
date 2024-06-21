from itertools import permutations

def solution(k0, dungeons):
    max_cnt = 0
    for perm in permutations(dungeons, len(dungeons)):
        cnt = 0
        k = k0
        for min_val, use in perm:
            if k < min_val: continue
            k -= use
            cnt += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt