# 소수 얻기
N = 4_000_000
is_prime = [True]*(N+1)

primes = []
for i in range(2,int(N)+1):
    if not is_prime[i]: continue
    primes.append(i)
    for j in range(2*i, N+1, i):
        is_prime[j] = False


# 투포인터
num = int(input())
M = len(primes)
j = 0
cnt = 0
total = primes[0]
for i in range(M):
    while j<M-1 and total < num:
        j+=1
        total += primes[j]
    if total == num: 
        cnt += 1
    total -= primes[i]
print(cnt)