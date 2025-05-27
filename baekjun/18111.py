import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
blocks = []
for _ in range(n):
    blocks += list(map(int, input().split()))

min_time = float('inf')
result_height = 0

total = 0
for i in blocks:
  total += i
avg = round(total/(n*m))
    
for target in range(avg//2,257):
    remove = 0
    add = 0
    for h in blocks:
        diff = h - target
        if diff > 0:
            remove += diff
        else:
            add -= diff

    if remove + b >= add:
        time = remove * 2 + add
        if time < min_time:
            min_time = time
            result_height = target
        elif time == min_time and target > result_height:
            result_height = target

print(min_time, result_height)
