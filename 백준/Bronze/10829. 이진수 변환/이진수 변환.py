n = int(input())
ans = ''
while n:
    ans += str(n%2)
    n //= 2
print(ans[::-1])