a = int(input())
b = int(input())
c = int(input())

A=str(a*b*c)
dic={}

for i in range(len(A)): # 각 숫자의 개수 카운팅
    if A[i] not in dic: 
        dic[A[i]]=1
    else:
        dic[A[i]]+=1

for i in range(10): # 각 숫자의 개수 출력
    if str(i) not in dic:
        print(0)
    else:
        print(dic[str(i)])