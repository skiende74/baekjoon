import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    line = input()
    if line=='.': break
    pat = line
    N = len(pat)
    pat = '#' + pat
    f = [-1]+[0]*N
    j = -1
    for i in range(1, N+1):
        while j>=0 and pat[j+1] != pat[i]: j = f[j]
        j += 1
        f[i] = j
    if N % (N-f[-1]) == 0: print(N//(N-f[-1])) 
    else:  print(1)