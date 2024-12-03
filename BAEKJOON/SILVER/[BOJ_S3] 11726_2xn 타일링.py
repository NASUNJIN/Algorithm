# f(1) = 1
# f(2) = 1 + 1 = 2
# f(3) = 1 + 2 = 3
# f(4) = 1 + 3 + 1 = 5
# f(5) = 1 + 4 + 3 = 8
# f(6) = 1 + 5 + 5 + 1 = 13

# f(n) = f(n-1) + f(n-2)

n = int(input())

rc = [0] * 1000
rc[1] = 1
rc[2] = 2
for i in range(3, n + 1):
  rc[i] = (rc[i - 1] + rc[i - 2])
print(rc[n] % 10007)


# n = int(input())

# res_dict = {'a' : n , 'b' : 0}
# count = 1

# def add_factorial(a,b) : 
#   res = 1
#   for i in range(1, a+b+1) :
#     res *= i

#   # print(res)
#   return res

# while(res_dict['a'] > 1) :
#   res_dict['a'] -= 2
#   res_dict['b'] += 1

#   factorial = add_factorial(res_dict['a'],res_dict['b'])
#   a_factorial = add_factorial(res_dict['a'],0)
#   b_factorial = add_factorial(res_dict['b'],0)

#   calc = factorial // (a_factorial * b_factorial)
#   count += calc

# print(count % 10007)