import sys
t = int(input())
n=[]
count = 0
rank = []
for _ in range(t):
  n.append(list(map(int,sys.stdin.readline().split())))

# for i in range(t):
#   for k in range(1):
#     print(n[i][k],n[i][k+1])
for i in range(t):
    cnt = 1
    for j in range(t):
        if n[i][0] < n[j][0] and n[i][1] < n[j][1]:
            cnt += 1
    rank.append(cnt)

print(*rank)