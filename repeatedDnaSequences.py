def findRepeatedDnaSequences(self, s: str) -> List[str]:
  l,r = 0, 9
  res = []
  hashmap = {}
  while r < len(s):
    dna = s[l:r+1]
    if dna not in hashmap:
      hashmap[dna] = 1
    else:
      hashmap[dna] += 1
      if dna not in res:
        res.append(dna)
    l += 1
    r += 1
  return res
