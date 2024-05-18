M, N = map(int,input().split())
Q = int(input())
stores = [list(map(int,input().split())) for _ in range(Q)]
dong = list(map(int,input().split()))

def dist(store1):
    store2 = dong
    store1,store2 = list(sorted((store1,store2), key = lambda x:x[0]))
    edge1, d1 = store1
    edge2, d2 = store2
    if edge1 == edge2: return abs(d1-d2)
    if (edge1,edge2) == (1,2):
        return N+abs(d1-d2)+min(d1,M-d1,d2,M-d2)*2
    if (edge1, edge2) == (3,4):
        return M+abs(d1-d2)+min(d1,d2,N-d1,N-d2)*2
    if (edge1,edge2) == (1,3):
        return d1+d2
    if (edge1,edge2) == (1,4):
        return M-d1+d2
    if (edge1, edge2) == (2,3):
        return d1+N-d2
    if (edge1, edge2) == (2,4):
        return M-d1+N-d2

print(sum(map(dist, stores)))