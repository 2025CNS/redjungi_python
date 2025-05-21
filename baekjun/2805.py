n,m = map(int,input().split())
h = list(map(int,input().split()))
def BinarySearch(h, target, start, end):
  if start > end:
    return end

  mid = (start + end) // 2
  total = 0
  for height in h:
    if height > mid:
      total += height - mid

  if total < target:
    return BinarySearch(h, target, start, mid - 1)
  else:
    return BinarySearch(h, target, mid + 1, end)


result = BinarySearch(h, m, 0, max(h))
print(result)