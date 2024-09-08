from itertools import permutations
def solution(numbers):
    N = len(numbers)
    answers = set()
    MAX = max(numbers)
    is_prime = prime()
    seq = [ permutations(numbers,k) for k in range(1, N+1)]
    seq2 = []
    for a in seq:
        seq2 += a
    for num_str in seq2:
        num = int(''.join(num_str))
        if is_prime[num]:
            answers.add(num)

    return len(answers)

def prime():
    N = 10_000_000
    is_prime = [True]*(N+1)
    is_prime[0], is_prime[1] = False, False
    is_prime[2] = True
    for i in range(2, N+1):
        if not is_prime[i]: continue
        for j in range(2*i, N+1, i):
            is_prime[j] = False
    return is_prime