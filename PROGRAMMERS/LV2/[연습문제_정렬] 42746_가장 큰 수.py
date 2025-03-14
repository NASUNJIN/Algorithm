def solution(numbers):
  answer = ''

  numbers = list(map(str, numbers))
  numbers.sort(key=lambda x: x*4, reverse=True)  # 같은숫자 4번씩 반복

  answer = ''.join(map(str, numbers))

  return str(int(answer))

numbers = list(map(int, input().split()))
print(solution(numbers))