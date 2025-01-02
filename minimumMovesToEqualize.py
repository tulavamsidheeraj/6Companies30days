def minimumTOEqualize(nums):
  nums.sort()
  mid=nums[len(nums)//2]
  for num in nums:
    ans+=abs(mid-num)
  return ans
