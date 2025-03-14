N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def sol1(N, A, B):   # A, B 배열 모두 건들였을 경우 
  answer = 0
  A.sort()
  B.sort(reverse=True)

  for i in range(N):
    answer += A[i] * B[i]

  return(answer)

def sol2(N, A, B):   # 문제에 주어진 대로 A 배열만 건들였을 경우
  answer = 0
  A.sort()

  for i in range(N):
    bMax = max(B)

    answer += A[i] * bMax
    B.remove(bMax)

  return(answer)

print(sol1(N, A, B))
print(sol2(N, A, B))