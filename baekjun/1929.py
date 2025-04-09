import sys
import math
input = sys.stdin.readline

m,n = map(int,input().split())

MAX = n
prime = [True for i in range(MAX+1)]

prime[1] = False

for i in range(2, int(math.sqrt(MAX))+1):
  if prime[i] == True:
    j = 2
    while i*j <= MAX:
      prime[i*j] = False
      j += 1
for i in range(m,len(prime)):
  if prime[i] == True:
    print(i)


