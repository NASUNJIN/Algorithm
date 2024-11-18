# 9 난쟁이 키
arr = [(int(input())) for _ in range(9)]
arr.sort()  # 오름차순 정렬
dwarfs = []  # 7 난쟁이

# DFS
def dfs(depth, start):
    if depth == 7:  # 만약 7번 재귀를 돌았다면
        if sum(dwarfs) == 100:  # 현재 저장된 7난쟁이의 합이 100일 경우
            print(dwarfs)
        else:  # 7명 뽑았는데 100이 아닐 경우
            return  # 재귀 실행하지 않고 종료
    
    for i in range(start, len(arr)):  # 시작 인덱스와 9명의 난쟁이가 있으므로 9번 돔
        dwarfs.append(arr[i]) # 난쟁이 한명 추가
        dfs(depth + 1, i + 1) 
        dwarfs.pop() 

dfs(0,0)