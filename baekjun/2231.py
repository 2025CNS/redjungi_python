n = int(input())
l = n-len(str(n))*9
if l < 0:
  l = 0
result = 0
for i in range(l, n+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
