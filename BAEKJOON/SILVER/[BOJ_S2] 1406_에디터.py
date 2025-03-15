import sys
input = sys.stdin.read
data = input().splitlines()

str = data[0].strip()
M = int(data[1].strip())
C = data[2 : 2 + M]   # data[2] ~ data[2+M]

# 스택 사용
def solution_stack(str, C):
  # 초기 문자열 저장
  left_stack = list(str)  # 커서 기준 왼쪽
  right_stack = []        # 커서 기준 오른쪽

  # 명령어 처리
  for command in C:
    if command == 'L':
      if left_stack:   # 왼쪽으로 이동
        right_stack.append(left_stack.pop())
    elif command == 'D':
      if right_stack:  # 오른쪽으로 이동
        left_stack.append(right_stack.pop())
    elif command == 'B':
      if left_stack:   # 왼쪽 문자 삭제
        left_stack.pop()
    elif command.startswith('P '):
      _, char = command.split()  # 문자 추가
      left_stack.append(char)

  result = ''.join(left_stack) + ''.join(reversed(right_stack))
  return result

# deque 사용
def solution_deque(str, M, C):
  from collections import deque

  # deque 사용하여 문자열 저장
  left = deque(str)
  right = deque()

  # 명령어 처리
  for command in C:
    if command == 'L':
      if left:  # 왼쪽으로 이동
        right.appendleft(left.pop())
    elif command == 'D':
      if right: # 오른쪽으로 이동
        left.append(right.popleft())
    elif command == 'B':
      if left:  # 왼쪽 문자 삭제
        left.pop()
    elif command.startswith('P '):
      _, char = command.split()
      left.append(char)

  result = ''.join(left) + ''.join(right)
  return result

print(solution_stack(str, M, C))
print(solution_deque(str, M, C))