from itertools import accumulate
N = int(input())
seq = [0] + list(map(int,input().split()))
p_sum = list(accumulate(seq))
def range_sum(i,j): return p_sum[j] - p_sum[i-1]
ans = 0

ans = max(ans, *[range_sum(2,N)+range_sum(i+1,N)-seq[i] for i in range(2, N)]) # 오른쪽 꿀통
ans = max(ans, *[range_sum(2,N-1)+seq[i] for i in range(2, N)]) # 가운데 꿀통
ans = max(ans, *[range_sum(1,N-1)+range_sum(1,i-1)-seq[i] for i in range(2, N)]) # 왼쪽 꿀통

print(ans)