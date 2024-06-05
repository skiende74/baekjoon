from itertools import combinations
def add(vec1, vec2): return (vec1[0]+vec2[0], vec1[1]+vec2[1])
def minus2(vec1, vec2): return (vec1[0]-2*vec2[0], vec1[1]-2*vec2[1])
def norm(vec): return (vec[0] **2 + vec[1]**2)**0.5

T = int(input())
for _ in range(T):
    N = int(input())
    seqs = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 10**9
    total_vec = sum([vec[0] for vec in seqs]), sum([vec[1] for vec in seqs])
    for vecs in combinations(seqs, N//2):
        res_vec = total_vec
        for vec in vecs:
            res_vec = minus2(res_vec, vec)
        ans = min(ans, norm(res_vec))
    print(ans)