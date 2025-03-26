s = [input() for _ in range(3)]
i = 0
for k in range(3):
  if s[k] == "FizzBuzz":
    continue
  elif s[k] == "Fizz":
    continue
  elif s[k] == "Buzz":
    continue
  else:
    i = int(s[k])-k+3
if i%3==0 and i%5==0:
  print("FizzBuzz")
elif i%3==0 and i%5!=0:
  print("Fizz")
elif i%3!=0 and i%5==0:
  print("Buzz")
else:
  print(i)