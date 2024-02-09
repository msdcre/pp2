#ex1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams_needed = float(input("Enter the amount in grams: "))
result_ounces = grams_to_ounces(grams_needed)
print(result_ounces)

#ex2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit_temperature = float(input("Enter the temperature in Fahrenheit: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_temperature)
print(celsius_result)

#ex3
def solve(numheads, numlegs):
    # Assuming chickens as c and rabbits as r

    for c in range(numheads + 1):
        r = numheads - c
        if 2 * c + 4 * r == numlegs:
            return c, r

numheads_given = 35
numlegs_given = 94
result = solve(numheads_given, numlegs_given)

if result:
    chickens, rabbits = result
    print(f"There are "
          f"{chickens} chickens and {rabbits} rabbits.")
else:
    print("No solution found.")

#ex4
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))

prime_numbers = filter_prime(numbers_list)
print("Prime numbers in the list:", prime_numbers)

#ex5
from itertools import permutations

def print_all_permutations(input_string):
    permuted_strings = [''.join(p) for p in permutations(input_string)]
    
    for permuted_string in permuted_strings:
        print(permuted_string)

user_input = input("Enter a string: ")
print_all_permutations(user_input)

#ex6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print(result)

#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input("Enter a list of numbers separated by spaces: ")
nums_list = list(map(int, user_input.split()))

result = has_33(nums_list)
print(result)

#ex8
def spy_game(nums):
    sequence_position = 0
    for num in nums:
        # Check if the current number matches the expected digit in the sequence
        if sequence_position == 0 and num == 0:
            sequence_position += 1
        elif sequence_position == 1 and num == 0:
            sequence_position += 1
        elif sequence_position == 2 and num == 7:
            return True
    return False
user_input = input("Enter a list of numbers separated by spaces: ")
nums_list = list(map(int, user_input.split()))
result = spy_game(nums_list)

print(result)

#ex9
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume
radius_input = float(input("Enter the radius of the sphere: "))
result_volume = sphere_volume(radius_input)
print(result_volume)

#ex10
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
user_input = input("Enter a list of elements separated by spaces: ")
original_list = list(map(int, user_input.split()))
result = unique_elements(original_list)
print( result)

#ex11
def is_palindrome(word):
    cleaned_word = ''.join(word.split()).lower()
    reversed_word = cleaned_word[::-1]
    return cleaned_word == reversed_word
user_input = input("Enter a word or phrase: ")
result = is_palindrome(user_input)
if result:
    print(f"YES")
else:
    print(f"NO")

#ex12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
user_input = input("Enter a list of integers separated by spaces: ")
input_numbers = list(map(int, user_input.split()))
histogram(input_numbers)

#ex13
# import random
# def guess_the_number():
#     print("Hello! What is your name?")
#     player_name = input()

#     print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")
#     secret_number = random.randint(1, 20)
#     guess_count = 0
#     max_guesses = 6
#     while guess_count < max_guesses:
#         print("Take a guess.")
#         player_guess = int(input())
#         guess_count += 1
#         if player_guess < secret_number:
#             print("Your guess is too low.")
#         elif player_guess > secret_number:
#             print("Your guess is too high.")
#         else:
#             print(f"Good job, {player_name}! You guessed my number in {guess_count} guesses!")
#             break
#     if guess_count == max_guesses:
#         print(f"Sorry, {player_name}. The number I was thinking of was {secret_number}.")
# guess_the_number()

#ex14
