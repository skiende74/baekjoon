import sys
lines = sys.stdin.read().split('\n')[:-1]

k = 0
while k<len(lines)-1:
    N, M = lines[k].split()
    N, M = int(N), int(float(M)*100+0.5)
    dp = [0]*(M+1)
    for line in lines[k+1:k+N+1]:
        c, p = line.split()
        c, p = int(c), int(float(p)*100+0.5)
        for i in range(p, M+1):
            dp[i] = max(dp[i], dp[i-p]+c)
    print(max(dp))
    k += N+1