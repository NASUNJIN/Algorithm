import math

def solution(fees, records):
  answer = []
  basic_time, basic_fee, per_min, plus_fee = fees

  # 차량 번호 기준 정렬
  records.sort(key = lambda x : int(x.split()[1]))
  car = {}  # 차량번호 : 주차시간
  for i in records:
    i = i.split()
    car[i[1]] = 0
      
  print(car)
  
  in_dic = {}  # 차량 번호 : 입차시간(분단위, -1일 경우 정산 완료)
  for i in records:
    i = i.split()
    t = i[0].split(':')
    in_time = int(t[0]) * 60 + int(t[1])
    
    if i[2] == "IN":  # 차량 번호에 맞춰 저장
      in_dic[i[1]] = in_time
    
    elif i[2] == "OUT": # 해당 차량 주차 시간 car에 저장
      if i[1] in in_dic.keys():
        car[i[1]] += in_time - in_dic[i[1]]
        in_dic[i[1]] = -1  # 정산 완료 차량
              
  print(in_dic)
      
  # 출차 하지 않은 차량
  for key, value in in_dic.items():
    if value != -1 : # 정산 안한 차량
      car[key] = car[key] + ((23 * 60 + 59) - in_dic[key])
  
  # 요금 계산
  car_fee = []
  for key, value in car.items():
    if value <= basic_time :  # 기본시간 이하
      car_fee.append((int(key), basic_fee))
    elif value > basic_time : # 기본시간 초과
      fee = basic_fee + math.ceil((value - basic_time) / per_min) * plus_fee
      car_fee.append((int(key), fee))
  
  print(car_fee)
  
  # 요금만 추출
  for key, fee in car_fee:
    answer.append(fee)
      
  return answer