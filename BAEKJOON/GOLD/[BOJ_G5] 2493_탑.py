# 탑세우는건 왼->오
# 레이저 나오는건 왼<-오 
# 수신은 무조건 첫번째 탑하나만 가능
# N : 탑의 수
# 레이저 수신 있으면 탑 없으면 0 출력
# 6 9 5 7 4 (높이)
# 0 0 2 2 4 (번째)

# 앞숫자 > 뒤숫자보다 클 경우 : 수신 (해당인덱스 + 1 입력)
# 첫번째숫자 <= 두번째숫자보다 작거나 같을 경우 : 수신X == 0

n = int(input())  # 탑 개수
arr = list(map(int, input().split()))  # 탑 높이

def solution(n, arr):  # 시간초과
  answer = [0] * n

  for i in range(n):
    for j in range(i - 1, -1, -1):  # 왼쪽으로 탐색
      if (arr[j] > arr[i]):   # 앞 > 뒤
        answer[i] = j + 1 
        break
  return answer



def stack(n, arr):  # 통과
  stack = []  # 인덱스, 높이
  answer = [0] * n

  for i in range(n):
    while stack:
      if (stack[-1][1] > arr[i]):  # 수신할 경우 (stack 최상단 > 현재 탑)
        answer[i] = stack[-1][0] + 1
        break
      else: # 수신X
        stack.pop()
    stack.append((i, arr[i]))  # 스택에 현재 탑 순서, 높이 추가

  return answer

# print("for문: ", solution(n, arr))
# print("stack: ", stack(n, arr))
# [0, 0, 2, 2, 4]

# 괄호 없이 출력
print(' '.join(map(str, stack(n, arr))))