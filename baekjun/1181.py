import sys
t = int(input())
word = []
for _ in range(t):
  word.append(sys.stdin.readline().strip())
word = list(set(word))
word.sort()
word.sort(key = len)

for i in word:
    print(i)


