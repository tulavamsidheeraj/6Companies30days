def numberOfSubarrays(self, nums: List[int], k: int) -> int:
  q=deque()
  diff=0
  ans=0
  diff=0
  last=-1
  for i in range(len(nums)):
    if nums[i]%2:
      q.append(i)
    if len(q)>k:
      last=q.popleft()
    if len(q)==k:
      diff=q[0]-last
      ans+=diff
  return ans
