t = int(input())
n=[]
for i in range(t):
  n.append(int(input()))

stack = []

for i in n:
  if i != 0:
    stack.append(i)
  if i == 0:
    stack.pop()
total =  0
for i in range(len(stack)):
  total += stack[i]
  
print(total)