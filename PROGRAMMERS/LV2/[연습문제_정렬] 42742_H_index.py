# H-index: 
# 논문 순위와 해당 논문 수 비교 (내림차순 정리)
# 순위 번호가 인용 수와 같거나 작아지는 지점

citations = list(map(int, input().split()))

def solution(citations):
  answer = 0
  citations.sort(reverse = True)
  
  # enumerate() : 인덱스 + 원소 접근
  for i, citation in enumerate(citations):
    if (i + 1 <= citation):
      h_index = i + 1
      answer = h_index
  
  return answer

print(solution(citations))