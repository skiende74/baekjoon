N = int(input())

negatives, zeros, positives = [],[],[]
nums = []
for _ in range(N):
    num = int(input())
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        positives.append(num)

negatives.sort(key=lambda x: -x)
positives.sort()

while True:
    if len(positives)<2: break
    a, b = positives.pop(), positives.pop()
    if a*b > a+b:
        nums.append(a*b)
    else:
        nums.append(a)
        nums.append(b)
while True:
    if len(negatives)<2: break
    a, b = negatives.pop(), negatives.pop()
    if a*b > a+b:
        nums.append(a*b)
    else:
        nums.append(a)
        nums.append(b)

if negatives:
    if len(zeros)==0:
        nums.append(negatives[0])
if positives:
    nums.append(positives[0])
print(sum(nums))