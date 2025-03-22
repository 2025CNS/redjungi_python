t = int(input())

for i in range(t):
    n, s = input().split()
    n = int(n)
    
    result = ""
    for char in s:
        result += char * n
    
    print(result)