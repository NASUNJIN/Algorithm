from itertools import permutations

# 소수 판별 함수
def is_prime(num):
  # 1은 소수가 아님
  if num < 2:
    return False
  
  # 2 ~ num의 제곱근까지 확인
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
    
  return True

def solution(numbers):
  # 소수를 저장할 집합 (중복 방지)
  primes = set()

  for i in range(1, len(numbers) + 1):
    # 길이가 i 인 모든 순열 생성
    perm = permutations(numbers, i)
    for p in perm:
      num = int(''.join(p))
      if is_prime(num):
        primes.add(num)

  return len(primes)

# 예제
print(solution("17"))  # 3
print(solution("011"))  # 2

# 다른 사람의 풀이
# 에라토스테네스의 체 사용한 소수 판별
def eratosthenes(numbers):
  a = set()  # 소수를 저장할 집합

  # 모든 가능한 순열을 생성하여 a 집합에 추가
  for i in range(len(numbers)):
    a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
  
  # 0과 1을 제거 (소수가 아님)
  a -= set(range(0, 2))

  # 에라토스테네스의 체를 사용하여 소수 판별
  for i in range(2, int(max(a) ** 0.5) + 1):
    a -= set(range(i * 2, max(a) + 1, i))

  return len(a)  # 소수의 개수 반환

print(eratosthenes("17"))
print(eratosthenes("011"))