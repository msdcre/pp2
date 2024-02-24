# #ex1
# def generate_squares(n):
#     for x in range(1, n + 1):
#         yield x ** 2
# n = int(input())
# squares_generator = generate_squares(n)
# for i in range(n):
#     print(next(squares_generator))

# #ex2
# def even_only(n):
#     for i in range(0, n + 1, 2):
#         yield i
# n = int(input())
# even_nums_generator = even_only(n)
# even_nums = list(even_nums_generator)
# result = ', '.join(map(str, even_nums))
# print(result)

# #ex3
# def divisible_by_34(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i
#         else:
#             yield
# n = int(input())
# divisibles = divisible_by_34(n)
# y=0
# for i in range(n):
#     p=next(divisibles)
#     if(p!=None):
#         print(p)
#         y+=1
# if(y==0):
#     print('there are no any dividers of 3 and 4')

# #ex4
# def squares(a, b):
#     for i in range(a, b + 1):
#         yield i ** 2
# a = int(input())
# b = int(input())
# nums = squares(a, b)
# for x in range(a, b + 1):
#     print(next(nums))

# #ex5
# def reverse(n):
#     for i in range(0, n + 1):
#         yield n - i
# n = int(input())
# rev_nums = reverse(n)
# for x in range(0, n + 1):
#     print(next(rev_nums), end=',' if x != n else '.')