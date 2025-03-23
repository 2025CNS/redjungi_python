c_n, name_n = map(int,input().split())
c = []
n = []
t_name = []
for i in range(c_n):
  c += input()
for i in range(name_n):
  n += input()

q = int(input())
for i in range(q):
  t_name += input()

print(c[2])