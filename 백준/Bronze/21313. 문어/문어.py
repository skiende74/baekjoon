N = int(input())
q, rem = divmod(N, 2)
print(' '.join((['1', '2']*q)+rem*['3']))