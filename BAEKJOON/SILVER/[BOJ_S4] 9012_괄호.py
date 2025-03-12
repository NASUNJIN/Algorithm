n = int(input())
arr = [input() for _ in range(n)]

# 갯수로 풀기
for i in arr:
  sum = 0
  isTrue = True

  for char in i:
    if char == '(' :
      sum += 1
    else :  # char == ')'
      sum -= 1
    
    if (sum < 0):
      isTrue = False
      break
  
  if (isTrue and sum == 0):
    print("YES")
  else:
    print("NO")


# 스택으로 풀기
for s in arr:
  stack = []
  isTrue = True

  for char in s:
    if char == '(':
      stack.append(char)  # # 스택에 '('추가
    else:  # char == ')'
      if stack:  # 스택에 '(' 있을 경우
        stack.pop()  # '(' 제거
      else:  # 스택에 아무것도 없을 경우
        isTrue = False  # ')' 더 많음
        break

  if isTrue and not stack:  # 스택 비어있고, 스택 인정될 경우
    print("YES")
  else:
    print("NO")