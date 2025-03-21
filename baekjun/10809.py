s = input()
alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
check = 0
for i in range(26):
  check = 0
  for k in range(len(s)):
    if alp[i] == s[k]:
      print(k,end=' ')
      check += 1
      break
  if check == 0:
    print(-1,end=" ")
