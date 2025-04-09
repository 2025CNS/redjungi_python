t = int(input())
result = []
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    count = 1
    while data:
        if data[0] < max(data):
            data.append(data.pop(0))

        else:
            if m == 0: break

            data.pop(0)
            count += 1

        m = m - 1 if m > 0 else len(data) - 1

    result.append(count)
for i in range(len(result)):
  print(result[i])