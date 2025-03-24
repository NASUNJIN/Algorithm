# (0, 1)   1
# (1, 3)   3
# (2, 7)   3 + 4
# (3, 17)  7 + 10   (7 + 3 + 7)
# (4, 41)  17 + 24  (17 + 7 +17)

# dp[i] = dp[i-1] + dp[i-1] + dp[i-2]
# dp[i] = 2dp[i-1] + dp[i-2]

# 첫째 줄에 사자를 배치하는 경우의 수를 9901로 나눈 나머지 출력
from sys import stdin
N = int(stdin.readline())

def solution(N):
  if N == 1 :
    return(3)
  else :
    dp = [1 for _ in range(N+1)]
    dp[1], dp[2] = 3, 7
    
    for i in range(3, N + 1):
      dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901
    return(dp[N])

print(solution(N))