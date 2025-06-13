t = int(input())
dic = {}
for _ in range(t):
  name, day, month, year = input().split()
  year = int(year)
  day = int(day)
  month = int(month)
  dic[name] = (year, month, day)

sorted_dic = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True)

print(sorted_dic[0][0])
print(sorted_dic[-1][0])
