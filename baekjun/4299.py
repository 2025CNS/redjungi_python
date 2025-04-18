a, s = list(map(int, input().split()))
x = (a + s)
y = (a - s)
if x % 2 != 0 or y % 2 != 0 or y < 0:
    print(-1)
else:
    x //= 2
    y //= 2
    print(max(x, y),min(x,y))