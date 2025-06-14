import sys
input = sys.stdin.readline

scores = []
for _ in range(8):
  scores.append(int(input()))

total = 0
scores_S = sorted(scores,reverse=True)
for i in range(5):
  total += scores_S[i]

result = []
print(total)
for i in scores_S[:5]:
  if i in scores:
    result.append(scores.index(i)+1)
    scores[scores.index(i)] = -1
result.sort()
print(*result)