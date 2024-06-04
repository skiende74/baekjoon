input_s = input()+'-'
nums = []
ops = []

i0=0
sign = 1
for i,s in enumerate(input_s):
    if s=='+' or s=='-':
        nums.append(int(input_s[i0:i]))
        if sign==-1: nums[-1] = min(nums[-1], -nums[-1])
        if s =='-': sign = -1
        ops.append(input_s[i])
        i0 = i+1
ops.pop()
print(sum(nums))