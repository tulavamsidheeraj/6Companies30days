def wiggleSort(self, nums: List[int]) -> None:
  n=len(nums)
  nums.sort()
  mid=(n-1)//2
  nums[::2],nums[1::2]=nums[mid::-1],nums[:mid:-1]
