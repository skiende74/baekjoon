num = int(input())
possible = num%2 ==0 or num>=5

def solve(num):
    ans, num = divmod(num,5)
    ans2 = num//2 if num%2 ==0 else num//2+2
    return ans+ans2
print(solve(num) if possible else -1)