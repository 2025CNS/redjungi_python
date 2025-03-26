import sys
import random
t = int(sys.stdin.readline())
s = []
for _ in range(t):
    n, d = map(str, sys.stdin.readline().rstrip().split())
    n = int(n)
    s.append((n, d))


s.sort(key = lambda x : x[0])
for i in range(t):
    for k in range(2):
        print(s[i][k],end=' ')
    print()