# #ex1
# from functools import reduce
# def mult_lists(nums):
#     result = reduce(lambda a, b: a * b, nums)
#     return result
# a = input()
# list = [int(num) for num in a.split()]
# if list:
#     result = mult_lists(list)
#     print(f"{result}")
# else:
#     print("empty list.")

# #ex2
# str = input()
# res_upper = 0
# res_lower = 0
# for x in str:
#     if x.islower():
#         res_lower += 1
#     elif x.isupper():
#         res_upper += 1
# print(f'the number of upper case letters: {res_upper}')
# print(f'the number of lower case letters: {res_lower}')

# #ex3
# def is_palindrome(s):
#     cleaned_str = ''.join(s.split()).lower()
#     return cleaned_str == cleaned_str[::-1]
# user_input = input()
# if is_palindrome(user_input):
#     print("the string is a palindrome.")
# else:
#     print("the string is not a palindrome.")

# #ex4
# import time, math
# def sq_root_timr(num, delayed_msec):
#     delayed_sec = delayed_msec / 1000
#     time.sleep(delayed_sec)
#     result = math.sqrt(num)
#     return result
# num_input = float(input())
# delay_input = int(input())
# result = sq_root_timr(num_input, delay_input)
# print(result)

# #ex5
# def all_true_elements(tuple_data):
#     return all(x for x in tuple_data)
# user_input = input()
# tuple_values = tuple(eval(x.strip()) if x.lower().strip() in ('true', 'false') else bool(int(x.strip())) for x in user_input.split(','))
# result = all_true_elements(tuple_values)
# print(f"{result}")