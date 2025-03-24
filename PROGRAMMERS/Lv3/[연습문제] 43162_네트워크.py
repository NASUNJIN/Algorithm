def solution(n, computers):
  visited = [False] * n
  network_count = 0
  
  # def 함수:
  def dfs(computer):
    # 현재 컴퓨터를 방문 처리
    visited[computer] = True

    # 모든 이웃 컴퓨터(0 ~ n-1)까지 순회하면서,
    for neighbor in range(n):
      print ("neighbor: ", neighbor)
      # 현재 컴퓨터와 연결되어있고, 방문하지 않은 컴퓨터에 대해 DFS 호출
      if(computers[computer][neighbor] == 1 and not visited[neighbor]):
        dfs(neighbor)

  # 모든 컴퓨터를 순회하면서 방문하지 않는 컴퓨터 찾기
  for i in range(n):
    # 만약 방문 X -> dfs 호출, 네트워크 개수 + 1
    if not visited[i]:
      dfs(i)
      network_count += 1


  # 네트워크 개수 반환
  return network_count

n = 3
computers = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0]]

print(solution(n, computers))