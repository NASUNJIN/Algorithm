def solution(new_id):
    answer = ''
    # 소문자
    new_id = new_id.lower()
    print(new_id)
    
    # 알파벳 소문자, 숫자,'-', '_', '.' 경우만 살리기
    # for i in new_id:
    #     if i.isalpha() or i.isdigit() or i in['-', '_', '.']:
    #         answer += i
    # print(answer)
    for i in new_id:
        if i.isalnum() or i in['-', '_', '.']:
            answer += i
    print(answer)
    
    # .. -> .
    while '..' in answer:
        answer = answer.replace('..', '.')
    print(answer)
    
    # 처음, 끝 . 제거
    # answer = answer.strip('.')
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    
    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
       
    # 빈문자열 a 대입
    if answer == '':
        answer = 'a'
    print(answer)
    
    # 16자 이상이면 16번째부터 삭제 + 마지막 .이면 .삭제
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    print(answer)
    
    # 길이가 2이하일 경우 마지막 글자를 길이가 3이 될때까지 반복
    while len(answer) < 3:
        answer += answer[-1]
    print(answer)
    
    return answer