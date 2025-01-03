def getHint(secret: str, guess: str) -> str:
  n=len(secret)
  visSecret=[0]*10
  visGuess=[0]*10
  bulls=0
  for i in range(n):
    if secret[i]==guess[i]:
      bulls+=1
      visSecret[int(secret[i])]+=1
      visGuess[int(guess[i])]+=1
  cowsAndBulls=0
  for i in range(10):
    if visSecret[i]!=0 and visGuess[i]!=0:
      cowsAndBulls+=min(visSecret[i],visGuess[i])
  return f"{bulls}A{abs(cowsAndBulls-bulls)}B"
