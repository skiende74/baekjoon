def processInputs():
    nums=[]
    for _ in range(int(input())):
        nums.append(int(input()))
    return nums
def processOutputs(nums):
    for num in nums:
        print(num)


numbers=processInputs()
numbers.sort()
processOutputs(numbers)