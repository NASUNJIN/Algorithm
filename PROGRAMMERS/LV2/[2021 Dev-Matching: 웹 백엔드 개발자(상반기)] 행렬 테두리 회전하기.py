def solution(rows, columns, queries):
  answer = []
  
  array = [[r * columns + (c + 1) for c in range(columns)] for r in range(rows)]
  # print(array)
  
  # 행열 이동
  for x1, y1, x2, y2 in queries:
    start = array[x1-1][y1-1]  # 왼쪽 위 값 저장
    small = start   # 최소값 초기화
    
    # 왼쪽
    for i in range(x1-1, x2-1):
      array[i][y1-1] = array[i+1][y1-1]
      small = min(small, array[i][y1-1])
    
    # 아래쪽
    for i in range(y1-1, y2-1):
      array[x2-1][i] = array[x2-1][i+1]
      small = min(small, array[x2-1][i])
    
    # 오른쪽
    for i in range(x2-1, x1-1, -1):
      array[i][y2-1] = array[i-1][y2-1]
      small = min(small, array[i][y2-1])
    
    # 위쪽
    for i in range(y2-1, y1-1, -1):
      array[x1-1][i] = array[x1-1][i-1]
      small = min(small, array[x1-1][i])
    
    # start 값을 제자리에 놓기
    array[x1-1][y1] = start
    
    # 최소값 추가
    answer.append(small)
        
  return answer