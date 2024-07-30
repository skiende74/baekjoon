N = 123456*2

is_prime = [True]*(N+1)
is_prime[1] = False

for i in range(2, N+1):
    if not is_prime[i]: continue
    for j in range(2*i, N+1, i): is_prime[j] = False

while True:
    n = int(input())
    if n == 0: break
    print(sum(is_prime[n+1:2*n+1]))