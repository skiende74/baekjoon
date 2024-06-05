N = int(input())
seq = list(map(int,input().split()))
seq.sort()
print(seq[2*N-1]-seq[N])