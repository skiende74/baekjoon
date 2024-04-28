from math import floor, ceil,log
N = 10**14
K = 10**7
A, B = map(int, input().split())
is_prime = [True]*(1+K)
is_prime[1] = False
primes = []
for i in range(2, 10**7+1):
    if not is_prime[i]: continue
    primes.append(i)
    for j in range(2*i, 10**7+1, i):
        is_prime[j] = False


cnt = 0
for i in primes:
    num = i*i
    while num<A:
        num *= i
    while A<= num <= B:
        cnt += 1
        num *= i
print(cnt)