import sys
t, m = map(int, sys.stdin.readline().rstrip().split())
n = int(input())
print(f"{(t + (m + n) // 60) % 24} {(m + n) % 60}")