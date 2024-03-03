path = r'C:\Users\Assel\Desktop\pp2_labs\lab1'
file_path = r'C:\Users\Assel\Desktop\pp2_labs\lab1\lab6\text.txt'
# file_path = r'C:\Users\Assel\Desktop\pp2_labs\lab1\K.txt'

# #ex1
# import os
# def list_directories_files(path):
#     print("Directories:")
#     for name in os.listdir(path):
#         fullname = os.path.join(path, name)
#         if os.path.isdir(fullname):
#             print(fullname)
#     print("\nFiles:")
#     for name in os.listdir(path):
#         fullname = os.path.join(path, name)
#         if os.path.isfile(fullname):
#             print(fullname)
#     print("\nAll Directories and Files:")
#     for name in os.listdir(path):
#         fullname = os.path.join(path, name)
#         print(fullname)
# list_directories_files(path)

# #ex2
# import os
# def check_path_access(path):
#     if os.path.exists(path):
#         print(f"The path '{path}' exists.")
#         if os.access(path, os.R_OK):
#             print(f"The path '{path}' is readable.")
#         else:
#             print(f"The path '{path}' is not readable.")
#         if os.access(path, os.W_OK):
#             print(f"The path '{path}' is writable.")
#         else:
#             print(f"The path '{path}' is not writable.")
#         if os.access(path, os.X_OK):
#             print(f"The path '{path}' is executable.")
#         else:
#             print(f"The path '{path}' is not executable.")
#     else:
#         print(f"The path '{path}' does not exist.")
# check_path_access(path)

# #ex3
# import os
# def analyze_path(path):
#     if os.path.exists(path):
#         print(f"The path '{path}' exists.")
#         filename = os.path.basename(path)
#         directory = os.path.dirname(path)
#         print(f"Filename: {filename}")
#         print(f"Directory: {directory}")
#     else:
#         print(f"The path '{path}' does not exist.")
# analyze_path(path)

# #ex4
# def count_lines(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             line_count = sum(1 for line in file)
#         return line_count
#     except FileNotFoundError:
#         return f"Error: File '{file_path}' not found."
#     except Exception as e:
#         return f"An error occurred: {e}"
# result = count_lines(file_path)
# print(result)

# #ex5
# def write_list_to_file(file_path, my_list):
#     try:
#         with open(file_path, 'w') as file:
#             for item in my_list:
#                 file.write(str(item) + '\n')
#     except Exception as e:
#         print(f"An error occurred: {e}")
# my_list = input((comma-separated): ).split(',')
# write_list_to_file(file_path, my_list)

# #ex6
# import string
# def generate_text_files():
#     for letter in string.ascii_uppercase:
#         file_name = f"{letter}.txt"
#         with open(file_name, 'w') as file:
#             file.write(f"This is the content of file {file_name}")
# generate_text_files()

# #ex7
# def copy_file(a_path, b_path):
#     try:
#         with open(a_path, 'r') as a_file:
#             content = a_file.read()
#         with open(b_path, 'w') as b_file:
#             b_file.write(content)
#     except FileNotFoundError:
#         print(f"Error: File '{a_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# a_path = input()
# b_path = input()
# copy_file(a_path, b_path)

# #ex8
# import os
# def delete_file(file_path):
#     try:
#         if not os.path.exists(file_path):
#             print(f"Error: File '{file_path}' not found.")
#             return
#         if not os.access(file_path, os.W_OK):
#             print(f"Error: No write access to '{file_path}'.")
#             return
#         os.remove(file_path)
#     except Exception as e:
#         print(f"An error occurred: {e}")
# delete_file(file_path)