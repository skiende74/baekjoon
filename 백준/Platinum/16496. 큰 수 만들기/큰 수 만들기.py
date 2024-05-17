from functools import cmp_to_key

def compare(a,b):
    if a+b<b+a: return 1
    if a+b==b+a: return 0
    return -1
N = int(input())
seq = input().split()
seq.sort(key=cmp_to_key(compare))

print(int(''.join(seq)))
