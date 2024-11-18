# # {1~49} 중 k(k>6)개 골라 집합 S 만들고 6개 번호 선택하는 프로그램
# # 입렵 마지막 줄에는 0이 주어짐

# from itertools import combinations

# array = []
# while True:
#     arr = list(map(int, input().split()))  # map(적용할 함수, 순회 가능한 객체)
    
#     if arr[0] == 0:
#         break
#     out = arr.pop(0)
#     print(arr)

#     if input() == "":
#         array = arr.append(arr)
#         print(array)
    
#     # for combi in combinations(arr, 6):
#     #     print(*combi)

#     print()

from itertools import combinations

array = []

while True:
    arr = list(map(int, input().split()))  # map() 함수 사용해서 정수 리스트로 변환해서 arr저장

    if arr[0] == 0:  # arr의 첫번째 요소가 0일 경우
        for arr in array:  # 
            # combinations(arr) = arr에서 6개로 구성된 조합 생성
            for combi in combinations(arr, 6):  
                print(*combi)  # combi는 tuple이어서 *을 사용하여 개별 요소로 전달
            print()
        break

    arr.pop(0)  # 첫번째 요소 제거
    array.append(arr)  # 입력받은 arr을 array 리스트에 추가
