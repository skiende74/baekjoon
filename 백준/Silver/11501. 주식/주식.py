
T = int(input())
for _ in range(T):
    N = int(input())
    seq = list(map(int,input().split()))
    
    max_seq = [0]*N
    max_val = 0
    for i in range(N)[::-1]:
        max_seq[i] = max_val
        max_val = max(max_val, seq[i])

    ans = 0
    for i, s in enumerate(seq):
        m = max_seq[i]
        ans += max(m-s, 0)
    print(ans)