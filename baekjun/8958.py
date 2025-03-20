t = int(input())
score = 0
combo = 1
result = []
for i in range(t):
  s = input()
  score = 0
  combo = 1
  for k in range(len(s)):
    if s[k] == "O":
      if combo > 1:
        score = score + combo
        combo +=1
      else:
        score = score+1
        combo = combo + 1
    else:
      combo = 1
  result.append(score)
  
for i in range(t):
  print(result[i])
  