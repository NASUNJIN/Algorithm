# 난쟁이의 키의 합이 100
# 9명의 난쟁이 키가 주어졌을 때 7명의 난쟁이를 찾아라
# 키 오름차순으로 출력
# 가능한 정답이 여러가지일 경우 아무거나 출력

# 입력 9개 받고 7개의 조합으로 나눈 뒤 합이 100인것만 출력

from itertools import combinations

list = []
for i in range(0, 9):  # 입력 9개 받음
    list.append(int(input()))

for combi in combinations(list, 7):  # list에서 7개 조합 받음
    if sum(combi) == 100:  # combi의 합이 100인 경우 
        for num in sorted(combi):  # 오름차순 정렬 및 조합 숫자 출력
            print(num)    
        break