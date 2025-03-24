rm = set()

for _ in range(10):
    n = int(input())
    rm.add(n % 42)

print(len(rm))