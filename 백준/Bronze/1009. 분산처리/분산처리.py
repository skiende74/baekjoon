d={1:1,2:4,3:4,4:2,5:1,6:1,7:4,8:4,9:2,0:1}
origin={1:1,2:6,3:1,4:6,5:5,6:6,7:1,8:6,9:1,0:10}
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    a %= 10
    b %= d[a]
    if b == 0: #b가 0이면 origin수.
        res = origin[a]
    else:
        res = (a**b)%10
        if res == 0: #0이면 10으로.
            res = 10
    print(res)