def solution(record):
  answer = []
  user = {}  # 유저아이디 : 닉네임
  
  
  for i in record:
    i = i.split()
    if i[0] in ["Enter", "Change"]:
      user[i[1]] = i[2]
      
  print(user)
  
  for i in record:
    i = i.split()
    if i[0] == "Enter":
      answer.append(f"{user[i[1]]}님이 들어왔습니다.")
    elif i[0] == "Leave":
      answer.append(f"{user[i[1]]}님이 나갔습니다.")
          
  print(answer)
      
  return answer