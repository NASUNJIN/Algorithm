a, b = map(int, input().split())

# 최대공약수
def A(a, b):
  while (b > 0) :
    (a, b) = (b, a % b)
  print(a)
  return a

# 최소공배수
B = (a * b) // A(a, b)
print(B)