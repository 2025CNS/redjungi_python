import sys
input = sys.stdin.readline
def dvdAndCnqr(paper,s,x,y):
  cnt = 0
  for i in range(x, x + s):
    for j in range(y, y + s):
      if paper[i][j] == 1:
        cnt += 1

  if cnt == s * s:
    return 0, 1
  elif cnt == 0:
    return 1, 0 

  half = s // 2
  w1, b1 = dvdAndCnqr(paper, half, x, y)
  w2, b2 = dvdAndCnqr(paper, half, x, y + half)
  w3, b3 = dvdAndCnqr(paper, half, x + half, y)
  w4, b4 = dvdAndCnqr(paper, half, x + half, y + half)

  return w1 + w2 + w3 + w4, b1 + b2 + b3 + b4




n = int(input())
paper=[]
for i in range(n):
  a = list(map(int,input().split()))
  paper.append(a)
print("\n".join(map(str,dvdAndCnqr(paper,n,0,0))))

