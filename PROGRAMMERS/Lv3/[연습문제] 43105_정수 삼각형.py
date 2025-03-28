# 아래층에서 올라가기
def solution(triangle):
    
  N = len(triangle) - 1

  while N > 0:  # N, N-1, ... 1
    for i in range(N):
      # 바로 윗층칸에 아래칸 두개중 큰 값 더함
      triangle[N-1][i] += max(triangle[N][i], triangle[N][i+1])
    # 층 하나 올리기
    N -=1
  
  return triangle[0][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))