N = int(input())
q = input()

def oper(op, num1,num2):
    if op == '+': return num1+num2
    if op == '-': return num1-num2
    if op == '*': return num1*num2

nums = list(map(int, q[::2]))
ops = q[1::2]
N = len(nums)

dp = [0]*N
dp[0] = nums[0]
if N==1:
    print(dp[0])
    quit()
dp[1] = oper(ops[0], nums[0], nums[1])
max_dp,min_dp = dp.copy(), dp.copy()
for i in range(2,N):
    possibles = [oper(ops[i-1], max_dp[i-1],nums[i]), oper(ops[i-1], min_dp[i-1],nums[i]), oper(ops[i-2],min_dp[i-2], oper(ops[i-1],nums[i-1],nums[i])), oper(ops[i-2],max_dp[i-2],oper(ops[i-1],nums[i-1],nums[i]))]
    max_dp[i] = max(possibles)
    min_dp[i] = min(possibles)
print(max_dp[N-1])