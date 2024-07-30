for _ in range(int(input())):
    num = int(input())
    ans = 'YES'
    for i in range(2, 10**6+1):
        if num % i == 0: ans = 'NO'
    print(ans)