T = int(input())
for _ in range(T):
    N = int(input())
    seq = [False]*(N+1)
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            seq[j] = not seq[j]
    print(sum(seq))    