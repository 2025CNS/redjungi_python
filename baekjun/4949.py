import sys
s = []
result = []
while True :
    s = input()
    stack = []

    if s == "." :
        break

    for i in s :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        result.append('yes')
    else :
        result.append('no')
for i in range(len(result)):
    print(result[i])