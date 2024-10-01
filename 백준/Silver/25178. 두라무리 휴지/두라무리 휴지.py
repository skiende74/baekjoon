from collections import Counter
N = int(input())
seq1 = input()
seq2 = input()
a1 = [ s for s in seq1[1:-1] if s not in 'aeiou']
a2 = [ s for s in seq2[1:-1] if s not in 'aeiou']

ans = ((seq1[0], seq1[-1]) == (seq2[0], seq2[-1])) and ''.join(a1) == ''.join(a2) and Counter(seq1) == Counter(seq2)
print('YES' if ans else 'NO')