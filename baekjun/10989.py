import sys
n = int(input())
num = [0]*10001
for i in range(n):
    number = int(sys.stdin.readline())
    num[number] = num[number] +1

for i in range(10001):
    if num[number]!=0:
        for j in range(num[i]):
            print(i)
