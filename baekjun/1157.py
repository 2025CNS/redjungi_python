word = input()
word = word.upper()
s_word = list(set(word))
result = []
for i in s_word:
  result.append(word.count(i))

cnt = 0
for i in result:
  if max(result) == i:
    cnt+=1
if cnt >= 2:
  print("?")
else:
  print(s_word[result.index(max(result))])

