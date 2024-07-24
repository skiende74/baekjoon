for _ in range(int(input())):
    N = int(input())
    seq = list(map(int,input().split()))
    
    total = 0
    ans = -10**9
    min_val = 0
    for s in seq:
        total += s
        ans = max(ans, total-min_val)
        if min_val > total: min_val = total
    print(ans)