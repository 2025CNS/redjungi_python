n,k = map(int,input().split())

def factorial(n):
  ans = 1
  for i in range(2,n+1):
    ans *= i
  return ans

print(factorial(n)//factorial(k)//factorial(n-k))