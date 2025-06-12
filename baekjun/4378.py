key1 = ['Q','W','E','R','T','Y','U','I','O','P','[',']','\\']
key2 = ['A','S','D','F','G','H','J','K','L',';','\'']
key3 = ['Z','X','C','V','B','N','M',',','.','/']
key4 = ['1','2','3','4','5','6','7','8','9','0','-','=']
while True:
  try:
    s = input()
  except EOFError:
    break
  if s == '':
    break
  for c in s:
    if c in key1:
      print(key1[key1.index(c)-1], end='')
    elif c in key2:
      print(key2[key2.index(c)-1], end='')
    elif c in key3:
      print(key3[key3.index(c)-1], end='')
    elif c in key4:
      print(key4[key4.index(c)-1], end='')
    else:
      print(c, end='')
  print()
