from collections import defaultdict

N, K = map(int,input().split())
seq = list(map(int,input().split()))

answer = 0
total =  0
prefix_sum = defaultdict(lambda: 0)
prefix_sum[0] = 1
for i in range(N):
    total += seq[i]
    answer += prefix_sum[total-K]
    prefix_sum[total] += 1
print(answer)