def is_palindrom():
    i,j = 0, N-1
    while i<j:
        if seq[i]==seq[j]: i,j = i+1, j-1
        else:
            if seq[i:j] == seq[i:j][::-1]: return 1
            if seq[i+1:j+1] == seq[i+1:j+1][::-1]: return 1
            return 2
    return 0
for _ in range(int(input())):
    seq = list(input())
    N = len(seq)
    print(is_palindrom())