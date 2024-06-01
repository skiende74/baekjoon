MOD = 10**9 + 7

def matrix_mult(A, B, mod):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def matrix_pow(mat, exp, mod):
    result = [[1, 0], [0, 1]]
    base = mat
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        exp //= 2
    return result

def count_ways(n):
    if n == 1: return 3
    base_matrix = [[2, 1], [1, 0]]
    result_matrix = matrix_pow(base_matrix, n - 1, MOD)
    return (result_matrix[0][0] * 3 + result_matrix[0][1]) % MOD

import sys
input = sys.stdin.readline
n = int(input().strip())

print(count_ways(n))
