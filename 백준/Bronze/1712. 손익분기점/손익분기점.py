A,B,C = map(int,input().split())
if C<=B:
    print(-1)
else:
    res = A//(C-B)
    print(res+1)