def solution(park, routes):
  answer = []  # (y, x)
  x, y = 0, 0;
  w, h = len(park[0]), len(park)
  op = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}   # (y, x)

  # 시작점
  for i in range(h) :
    for j in range(w) :
      if park[i][j] == "S":
        x, y = j, i
        break

  # 좌표 이동
  for r in routes:
    d, n = r.split(" ");    # 방향, 이동횟수
    dx, dy = x, y   # 현재 위치

    for i in range(int(n)):
      # 이동할 위치
      nx = x + op[d][1]
      ny = y + op[d][0]

      # 이동할 수 있을 경우
      if (0 <= nx <= w-1) and (0 <= ny <= h-1) and (park[ny][nx] != "X"):
        x, y = nx, ny
        answer = y, x
      else:   # 없을 경우
        x, y = dx, dy
        answer = y, x
        break

  return answer