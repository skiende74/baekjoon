from bisect import bisect_right
T = int(input())
N = 2**16
sum_val = [0]*N
for i in range(1, N):
    sum_val[i] = sum_val[i-1] + i
for _ in range(T):
    a, b = map(int,input().split())
    num = b-a
    i = bisect_right(sum_val, num//2) -1
    if num == 2 * sum_val[i]: # 정확히 일치
        print(2*i)
    elif num > 2 * sum_val[i] + i + 1: # i+1 하나로는 빡세서 두개더해줌
        print(2*i+2)
    else:
        print(2*i+1) # 하나만 더해주면된다