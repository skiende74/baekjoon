nums = list(map(int,input()))
is_possible = sum(nums) % 3 == 0 and nums.count(0)>=1

nums.sort(reverse=True)
ans = ''.join(map(str,nums))
print(ans if is_possible else -1)