import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num_li = list(map(int,input().split()))
prefix = [0]*(n+1)
for i in range(1,n+1):
  prefix[i] = prefix[i-1]+num_li[i-1]
result = []
for i in range(m):
  start,end = map(int,input().split())
  result.append(prefix[end]-prefix[start-1])
print("\n".join(map(str,result)))