import sys
input = sys.stdin.readline
k,n = map(int,input().split())
x = [int(input()) for _ in range(k)]


result = []
start = 0
end = max(x)+1
while 1:
  if start+1 == end:
    break
  mid = (start+end)//2
  count = 0
  for i in range(len(x)):
    count += x[i]//mid
  if count >= n:
    result.append(mid)
    start=mid
  else:
    end=mid
  
print(max(result))
    