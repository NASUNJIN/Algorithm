# 대문자로 다 변환 > 갯수 세기 > 같 ? 많은거 대문자
A = input().upper() # 대문자 변환
sA = list(set(A.upper())) # 중복 글자 제외 set()함수 사용
li = []

for i in sA:
    count = A.count(i)
    li.append(count)

if li.count(max(li)) > 1 :  # max 함수 사용해서 갯수가 2개 이상이면 중복
    print("?")
else :
    print(sA[li.index(max(li))]) # li 중 가장 큰 숫자의 인덱스로 sA의 글자 유추
