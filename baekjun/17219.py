import sys
input = sys.stdin.readline
n,m = map(int,input().split())
site = {}
result = []
for _ in range(n):
  s, p = input().split()
  site[s] = p
for _ in range(m):
  q = input().strip()
  result.append(site[q])

print("\n".join(result))
