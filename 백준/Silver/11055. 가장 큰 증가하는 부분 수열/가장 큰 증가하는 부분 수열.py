N = int(input())
seq = list(map(int, input().split()))
dp = seq.copy()
def solve():
    if N==1: return seq[0]

    for i in range(1,N):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j]+seq[i])
    return max(dp)

print(solve())