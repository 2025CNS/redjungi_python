import sys
input = sys.stdin.readline

n = int(input())
x=list(map(int,input().split()))
x_sort = sorted(set(x))
dic = {}

dic = {}
dic = {value: idx for idx, value in enumerate(x_sort)}

# 출력
print(' '.join(str(dic[i]) for i in x))
