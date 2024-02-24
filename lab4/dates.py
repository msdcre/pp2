# #ex1
# from datetime import datetime, timedelta
# x = datetime.now()
# y = x - timedelta(5)
# print(x, y)

# #ex2
# from datetime import datetime, timedelta
# today = datetime.now()
# yesterdat = today - timedelta(1)
# tomorrow = today + timedelta(1)
# print(yesterdat.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d'), tomorrow.strftime('%Y-%m-%d'), sep='\n')

# #ex3
# from datetime import datetime
# date = datetime.now()
# print(date.strftime('%Y-%m-%d %H:%M:%S'))

# #ex4
# from datetime import datetime
# def date_dif(x, y):
#     delta = x - y
#     return abs(int(delta.total_seconds()))
# date1 = input("in (YYYY-MM-DD HH:MM:SS) format :")
# date2 = input("in (YYYY-MM-DD HH:MM:SS) format :")
# date_format = "%Y-%m-%d %H:%M:%S"
# x = datetime.strptime(date1, date_format)
# y = datetime.strptime(date2, date_format)
# dif_sec = date_dif(x, y)
# print(f"{dif_sec} seconds")