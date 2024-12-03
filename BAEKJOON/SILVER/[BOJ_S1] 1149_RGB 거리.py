# 백준 1149 RGB거리

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 현재 집 = 겹치지 않는 색을 칠한 이전 집 중 최소 비용 + 현재 집 비용
for i in range(1, n):
  arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
  arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
  arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
  print(arr)

print(arr[n-1])
print(min(arr[n-1]))

# 첫 행을 첫번째 집에 각 색을 칠하는 비용으로 먼저 채워놓고, 다음 집에 이전 집에서 칠한 색을 제외한 색 중 더 저렴한 색을 칠합니다.

# 첫 행을 제외한 나머지 행에 대해서 이 과정을 수행하므로 1부터 n-1까지 반복하고, 추가로 각 과정에서 현재 집을 해당 색으로 칠하는 비용을 더해줍니다.

# 마지막 행에서 누적된 값들 중 가장 적은 비용을 출력합니다.

# import sys
# input = sys.stdin.readline

# data = []
# n = int(input())
# for _ in range(n):
#   data.append(list(map(int, input().split())))

# for i in range(1,n):
#   data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
#   data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
#   data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]

# print(min(data[n-1]))