def findWinner(n,k):
  
  def recursion(n, k):
    if n == 1:
      return 0
    return (recursion(n - 1, k) + k) % n
  return recursion(n, k) + 1

# DP APPROACH

def findWinner(n,k):
  ans=0
  for p in range(2,n+1):
    ans=(ans+k)%p
  return ans+1
