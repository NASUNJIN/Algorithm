def solution(s):
    stack = []
    
    for i in s:
        if (i == '('):
            stack.append(i)  # 스택에 '(' 추가
        else:  # i == ')'
            if stack:  # 스택에 '(' 있을 경우
                stack.pop()  # '(' 제거
            else:  # 스택에 아무것도 없을 경우
                return False
            
    # 스택이 비어있을 경우 True, 아니면 False
    return len(stack) == 0

s = input()
result = solution(s)
print(result)