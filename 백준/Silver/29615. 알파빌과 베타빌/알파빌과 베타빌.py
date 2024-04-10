N, M = map(int,input().split())
seq = list(map(int,input().split()))
friends = list(map(int,input().split()))

count = 0
while True:
    p_first, f_last = None, None

    for i, s in enumerate(seq):
        if s not in friends and p_first == None:
            p_first = i
        if s in friends:
            f_last = i
    if p_first == None: break
    if p_first > f_last: break
    seq[f_last], seq[p_first] = seq[p_first], seq[f_last]
    count += 1
print(count)