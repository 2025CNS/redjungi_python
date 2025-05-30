from collections import defaultdict

n = int(input())
s = list(map(int,input().split()))
left = 0
right = 0
count = defaultdict(int)

max_len = 0
while right<n:
  count[s[right]] += 1
  
  while len(count) > 2:
    count[s[left]] -= 1
    if count[s[left]] == 0:
      del count[s[left]]
    left += 1
  max_len = max(max_len,right-left+1)
  
  right += 1
print(max_len)
  
    

