for _ in range(int(input())):
    N = int(input())
    seq = [1 for i in range(1,N+1) if int(i**0.5)**2==i]
    print(sum(seq))