from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

nums = []
for num in arr:
    pos = bisect_left(nums, num)
    if pos == len(nums):
        nums.append(num)
    else: nums[pos] = num

print(len(nums))
